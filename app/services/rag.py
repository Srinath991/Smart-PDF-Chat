from langchain_google_community.gcs_file import GCSFileLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from services.pinecone import get_vector_store
from services.vertexai import generate_answer
from services.gcs import upload_to_gcs
from uuid import uuid4
from core.config import settings
async def process_document(file):
    id=f"{uuid4()}"
    filename = f"{id}.pdf"
    gcs_path = upload_to_gcs(file, filename)

    loader = GCSFileLoader(
        project_name=settings.GOOGLE_PROJECT,
        bucket=settings.GCS_BUCKET,
        blob=gcs_path,
        loader_func=PyMuPDFLoader
    )
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)

    vector_store = get_vector_store(id)
    vector_store.add_documents(chunks,namespace=id)

    return {"message": "Uploaded and indexed", "namespace": id}


async def query_document(query: str,namespace:str):
    vector_store = get_vector_store(namespace)
    retriever = vector_store.as_retriever(search_kwargs={"k": 5},)
    results = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in results])
    prompt = f"""You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use atleast three sentences and keep the answer concise.
    if the question is out of context then use your knowledge to answer to question by not considering the context.
Question: {query}
Context: {context}
Answer:
"""
    return {"response":generate_answer(prompt)}
