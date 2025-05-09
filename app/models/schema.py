from pydantic import BaseModel, Field
from uuid import UUID

class QueryRequest(BaseModel):
    question: str
    namespace: UUID = Field(..., description="Namespace as a UUID (converted to string internally)")
