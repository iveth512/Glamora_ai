import os
import glob
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Configuración
DOCS_PATH = os.path.join(os.path.dirname(__file__), 'RAG')
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'  # Puedes cambiar el modelo si lo deseas
INDEX_PATH = os.path.join(os.path.dirname(__file__), 'faiss_index.bin')

# 1. Cargar documentos

def load_documents(path):
    files = glob.glob(os.path.join(path, '*.txt'))
    docs = []
    metadatas = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            docs.append(text)
            metadatas.append({'filename': os.path.basename(file)})
    return docs, metadatas

# 2. Crear embeddings

def embed_documents(docs, model_name=EMBEDDING_MODEL):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(docs, show_progress_bar=True)
    return embeddings

# 3. Guardar y cargar índice FAISS

def save_faiss_index(embeddings, metadatas, path=INDEX_PATH):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss.write_index(index, path)
    # Guardar metadatas
    np.save(path + '.meta.npy', np.array(metadatas, dtype=object))

def load_faiss_index(path=INDEX_PATH):
    index = faiss.read_index(path)
    metadatas = np.load(path + '.meta.npy', allow_pickle=True)
    return index, metadatas

# 4. Consulta

def query_rag(question, top_k=3, model_name=EMBEDDING_MODEL, index_path=INDEX_PATH):
    model = SentenceTransformer(model_name)
    q_emb = model.encode([question])
    index, metadatas = load_faiss_index(index_path)
    D, I = index.search(q_emb, top_k)
    results = []
    for idx in I[0]:
        results.append(metadatas[idx])
    return results

def get_relevant_context(question, top_k=3, model_name=EMBEDDING_MODEL, index_path=INDEX_PATH, docs_path=DOCS_PATH):
    """
    Devuelve el texto de los documentos más relevantes para la pregunta.
    """
    model = SentenceTransformer(model_name)
    q_emb = model.encode([question])
    index, metadatas = load_faiss_index(index_path)
    D, I = index.search(q_emb, top_k)
    # Cargar todos los documentos
    docs, _ = load_documents(docs_path)
    # Mapear filename a texto
    filename_to_text = {}
    files = glob.glob(os.path.join(docs_path, '*.txt'))
    for file, text in zip(files, docs):
        filename_to_text[os.path.basename(file)] = text
    # Obtener textos relevantes
    context = []
    for idx in I[0]:
        filename = metadatas[idx]['filename']
        context.append(filename_to_text.get(filename, ""))
    return "\n".join(context)

if __name__ == "__main__":
    # Paso 1: Indexar documentos (solo la primera vez o cuando cambien los docs)
    docs, metadatas = load_documents(DOCS_PATH)
    print(f"Documentos encontrados: {len(docs)}")
    embeddings = embed_documents(docs)
    save_faiss_index(np.array(embeddings).astype('float32'), metadatas)
    print("Indexación completada.")

    # Paso 2: Consulta de ejemplo
    pregunta = input("Escribe tu pregunta: ")
    resultados = query_rag(pregunta)
    print("\nDocumentos más relevantes:")
    for r in resultados:
        print(f"- {r['filename']}")
