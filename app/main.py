from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Body
from pydantic import BaseModel
import sys
import os

# Asegura que el directorio raíz esté en sys.path para importar LLM_v3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from LLM_v3 import generar_respuesta

app = FastAPI()

# Montar archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar plantillas Jinja2
templates = Jinja2Templates(directory="templates")

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
    respuesta = generar_respuesta(data.pregunta)
    return {"respuesta": respuesta}
