# Glamora AI - Asistente de Moda con IA

Glamora AI es un asistente conversacional de moda que utiliza inteligencia artificial para responder preguntas, inspirar outfits y brindar consejos de estilo. El proyecto incluye una interfaz web moderna y responsiva, así como un backend que conecta con la API de OpenAI.

## Características

- **Chat interactivo** con animaciones y diseño profesional.
- **Modo claro/oscuro** con interruptor personalizado.
- **Like animado** en respuestas de Glamora.
- **Soporte para emojis** y sonidos en las interacciones.
- **Scroll personalizado** en el historial del chat.
- **Frontend responsivo** y visualmente atractivo.
- **Backend seguro**: la API key de OpenAI se almacena en un archivo `.env` (no se sube al repositorio).

## Estructura del Proyecto

```
├── app/
│   └── templates/
│       └── index.html         # Interfaz web principal
├── LLM_v3.py                  # Script de prueba para OpenAI
├── .env                       # Variables de entorno (NO subir al repo)
├── README.md                  # Este archivo
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

### 4. Configura tu API key de OpenAI
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```
OPENAI_API_KEY=tu_api_key_aqui
```

### 5. Ejecuta el script de prueba
```sh
python LLM_v3.py
```

### 6. Levanta el servidor web (FastAPI + Uvicorn)
Desde la carpeta `app`:
```sh
cd app
uvicorn main:app --reload
```

### 7. Abre la web
Accede a la interfaz en tu navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Seguridad
- **Nunca subas tu archivo `.env` al repositorio.**
- El archivo `.env` ya está en el `.gitignore` por defecto.

## Créditos
Bootcamp de Inteligencia Artificial TALENTOTECH

## Iniciar API
pip install -r requirements.txt
uvicorn main:app --reload

---

¡Disfruta tu experiencia con Glamora AI y lleva tu estilo al siguiente nivel!
