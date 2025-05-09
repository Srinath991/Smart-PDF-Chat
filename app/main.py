from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from api.v1.router import api_router
import uvicorn
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request

templates = Jinja2Templates(directory="app/templates")

load_dotenv()

app = FastAPI(title="RAG System with GCS, Pinecone, and Vertex AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(api_router, prefix="/api/v1")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "chat_history": []})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

