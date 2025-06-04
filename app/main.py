from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Body
from pydantic import BaseModel
import sys
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Asegura que el directorio raíz esté en sys.path para importar LLM_v3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from LLM_v3 import generar_respuesta
from rag_pipeline import get_relevant_context

app = FastAPI()

# Montar archivos estáticos (CSS, JS, imágenes)
import os
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Configurar plantillas Jinja2
import os
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)

# Ruta para la página principal (frontend)
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ejemplo de endpoint backend (API)
@app.get("/api/saludo")
async def saludo(nombre: str = "Mundo"):
    return {"mensaje": f"Hola, {nombre}!"}

# Modelo para la petición de chat
class ChatRequest(BaseModel):
    pregunta: str

# Endpoint para el chatbot
@app.post("/api/chat")
async def chat_endpoint(data: ChatRequest):
    # Obtener contexto relevante usando RAG
    context = get_relevant_context(data.pregunta, top_k=3)
    respuesta = generar_respuesta(data.pregunta, context=context)
    return {"respuesta": respuesta}

# Modelo para la petición de llamada
class CallRequest(BaseModel):
    telefono: str

# Endpoint para solicitar llamada a ElevenLabs
@app.post("/api/llamar")
async def llamar_endpoint(data: CallRequest):
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID")
    AGENT_PHONE_ID = os.getenv("ELEVENLABS_AGENT_PHONE_ID")
    url = "https://api.elevenlabs.io/v1/convai/twilio/outbound-call"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "agent_id": AGENT_ID,
        "agent_phone_number_id": AGENT_PHONE_ID,
        "to_number": data.telefono
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200:
            return {"success": True, "message": "Llamada solicitada correctamente"}
        else:
            return {"success": False, "message": response.text}
    except Exception as e:
        return {"success": False, "message": str(e)}
