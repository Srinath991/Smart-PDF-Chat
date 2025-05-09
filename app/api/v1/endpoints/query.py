from fastapi import APIRouter
from models.schema import QueryRequest
from services.rag import query_document

router = APIRouter()

@router.post("/query")
async def ask_question(req: QueryRequest):
    return await query_document(req.question,str(req.namespace))
