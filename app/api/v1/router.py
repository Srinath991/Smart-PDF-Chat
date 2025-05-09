from fastapi import APIRouter
from .endpoints import upload, query

api_router = APIRouter()
api_router.include_router(upload.router, tags=["Upload"])
api_router.include_router(query.router, tags=["Query"])
