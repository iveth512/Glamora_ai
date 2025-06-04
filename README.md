# Glamora AI - Asistente de Moda con IA

Glamora AI es un asistente conversacional de moda que utiliza inteligencia artificial para responder preguntas, inspirar outfits y brindar consejos de estilo. El proyecto incluye una interfaz web moderna y responsiva, así como un backend que conecta con la API de OpenAI y un sistema RAG para respuestas basadas en documentos.

## Características

- **Chat interactivo** con animaciones y diseño profesional.
- **Modo claro/oscuro** con interruptor personalizado.
- **Like animado** en respuestas de Glamora.
- **Soporte para emojis** y sonidos en las interacciones.
- **Scroll personalizado** en el historial del chat.
- **Frontend responsivo** y visualmente atractivo.
- **Botón de llamada flotante** tipo "isla", fijo en escritorio y movible en móvil.
- **Backend seguro**: la API key de OpenAI y ElevenLabs se almacena en un archivo `.env` (no se sube al repositorio).
- **RAG**: Respuestas aumentadas con recuperación de contexto desde documentos `.txt`.

## Estructura del Proyecto

```
├── app/
│   ├── main.py
│   ├── static/
│   └── templates/
│       └── index.html         # Interfaz web principal
├── LLM_v3.py                  # Script de prueba para OpenAI
├── rag_pipeline.py            # Pipeline de indexado y consulta RAG
├── .env                       # Variables de entorno (NO subir al repo)
├── requirements.txt           # Dependencias del proyecto
├── Dockerfile
├── docker-compose.yml
├── .gitignore                 # Ignora archivos sensibles y temporales
├── README.md                  # Este archivo
├── RAG/                       # Carpeta para tus documentos .txt
```

## Instalación y Uso

### 1. Clona el repositorio

### 2. Crea y activa el entorno virtual (Windows)
```sh
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instala las dependencias
```sh
pip install -r requirements.txt
```

### 4. Configura tus claves en `.env`
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (usa tus propias claves, nunca compartas tus API keys):
```
OPENAI_API_KEY=tu_api_key_openai
ELEVENLABS_API_KEY=tu_api_key_elevenlabs
ELEVENLABS_AGENT_ID=agent_XXXXXXXXXXXXXXX
ELEVENLABS_AGENT_PHONE_ID=phnum_XXXXXXXXXXXXXXX
```

### 5. Indexa tus documentos (solo la primera vez o cuando cambien)
Coloca tus archivos `.txt` en la carpeta `RAG/` y ejecuta:
```sh
python rag_pipeline.py
```

### 6. Levanta el servidor web (FastAPI + Uvicorn)
Desde la raíz del proyecto:
```sh
uvicorn app.main:app --reload
```

### 7. Abre la web
Accede a la interfaz en tu navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Seguridad
- **Nunca subas tu archivo `.env` al repositorio.**
- El archivo `.env` ya está en el `.gitignore` por defecto.
- **Nunca publiques tus API keys en foros, repositorios públicos ni README.**

## Llamadas automáticas con ElevenLabs
- El botón flotante de llamada permite solicitar una llamada automática a través de la API de ElevenLabs.
- En móvil, puedes mover el botón por la pantalla; en escritorio, es fijo.
- El backend expone el endpoint `/api/llamar` para gestionar la solicitud de llamada.

## Integración RAG (Retrieval-Augmented Generation)

El sistema incorpora RAG para responder usando información relevante de documentos `.txt` que coloques en la carpeta `RAG/`.

### ¿Cómo funciona?
1. Cuando el usuario hace una pregunta, el sistema busca los documentos más relevantes usando embeddings y FAISS.
2. El texto de esos documentos se pasa como contexto al modelo OpenAI.
3. El modelo responde usando tanto el contexto como su conocimiento general.

### Estructura adicional para RAG
- `RAG/` — Carpeta donde debes colocar tus documentos `.txt`.
- `rag_pipeline.py` — Script para indexar y consultar documentos usando embeddings y FAISS.

### Indexar documentos (solo la primera vez o cuando cambien los documentos)

Ejecuta:
```sh
python rag_pipeline.py
```
Esto generará el índice vectorial necesario para el RAG.

### Uso del endpoint `/api/chat` con RAG

El endpoint `/api/chat` ahora utiliza el contexto de los documentos más relevantes para responder. Ejemplo de petición:
```json
{
  "pregunta": "¿Cuál es el protocolo recomendado?"
}
```
La respuesta usará el contexto de los documentos `.txt` que hayas indexado.

## Despliegue en Docker

1. Construye la imagen:
   ```sh
   docker build -t proyectofinalv5 .
   ```
2. Ejecuta el contenedor:
   ```sh
   docker run -p 8000:8000 proyectofinalv5
   ```
3. O usa docker-compose:
   ```sh
   docker-compose up --build
   ```

## Subir la imagen a Docker Hub
1. Inicia sesión:
   ```sh
   docker login
   ```
2. Etiqueta la imagen:
   ```sh
   docker tag proyectofinalv5 tuusuario/glamora:latest
   ```
3. Sube la imagen:
   ```sh
   docker push tuusuario/glamora:latest
   ```

## Créditos
- Iveth Ramírez Palacios

---
¡Disfruta tu experiencia con Glamora AI y lleva tu estilo al siguiente nivel!
