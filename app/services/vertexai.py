from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(model="gemini-2.0-flash")

def generate_answer(prompt: str):
    return llm.invoke(prompt)


