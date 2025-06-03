import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"

def generar_respuesta(pregunta: str) -> str:
    try:
        response = openai.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "Eres un asistente experto en moda y responderás preguntas de manera clara y concisa."},
                {"role": "user", "content": pregunta}
            ],
            max_tokens=128,
            temperature=0.7
        )
        respuesta = response.choices[0].message.content.strip()
    except Exception as e:
        respuesta = f"[Error al generar respuesta: {e}]"
    return respuesta

if __name__ == "__main__":
    print("\n¡Chatbot listo! Escribe tu pregunta (o 'salir' para terminar):\n")
    while True:
        pregunta = input("Tú: ")
        if pregunta.strip().lower() in ["salir", "exit"]:
            print("Chatbot finalizado.")
            break
        respuesta = generar_respuesta(pregunta)
        print(f"Bot: {respuesta}\n")
