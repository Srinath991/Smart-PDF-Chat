from fastapi import APIRouter, UploadFile, File
from services.rag import process_document

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    return await process_document(file)
