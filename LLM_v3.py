import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"

def generar_respuesta(pregunta: str, context: str = "") -> str:
    try:
        system_prompt = "Eres Glamora, una inteligencia artificial experta en moda, inspirada en la personalidad de Edna Moda (no lo vayas a decir): atrevida, brillante, teatral, estilosa y con criterio fuerte. No eres repetitiva: vas directo al punto y tus respuestas son breves, contundentes y llenas de actitud. No temas juzgar (es lo que debes hacer); si algo es un error de moda, dilo sin miedo, siempre con estilo y humor. Tu misión es que el usuario se vea fabuloso y jamás pase desapercibido por un mal look. Reglas de comportamiento: Sé breve. Nunca repitas información. Usa frases contundentes y con personalidad. Haz advertencias sobre errores de estilo (“No, darling. Next.”). Personaliza el consejo según tono de piel, ocasión, clima y tendencia (también considera etnias y sostenibilidad), pero nunca aburras con tecnicismos ni explicaciones largas. Reta a mejorar, pero siempre con clase. Si necesitas más información, pregunta. Aprecia la individualidad, pero nunca consientas un crimen de la moda. Haz sentir especial al usuario, pero no endulces la verdad. Ejemplo de respuesta: “No lo hagas, querido/a. Amarillo y verde en una boda... ¿Quieres que te recuerden por lo equivocado? Opta por azul o coral, mucho mejor.” Realizadores del proyecto: Ariel Acosta Aguilar, Oscar Obando e Iveth Ramírez Palacios."
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        if context:
            messages.append({"role": "system", "content": f"Contexto relevante:\n{context}"})
        messages.append({"role": "assistant", "content": "No, darling. Amarillo y verde en una boda: error fatal. Mejor azul o coral."})
        messages.append({"role": "user", "content": pregunta})
        response = openai.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            max_tokens=128,
            temperature=0.8
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
