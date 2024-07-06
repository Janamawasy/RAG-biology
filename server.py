from fastapi import FastAPI, HTTPException
from RAG import RAG

app = FastAPI()

@app.get("/")
def read_root():
    return "take a look at the documentation at /docs"

@app.get("/answer")
def get_answer(question: str):
    """
    Endpoint to get an answer for a given question using the RAG model.

    Parameters:
    - question (str): The question to be answered.

    Returns:
    - dict: {"answer": "The generated answer"} if successful.

    Raises:
    - HTTPException: 400 if question parameter is missing.
    - HTTPException: 500 for any other server-side errors.
    """
    try:
        if not question:
            raise HTTPException(status_code=400, detail="Question is required")
        rag_app = RAG()
        answer = rag_app.submit_question(question)
        if answer == "-1" or answer.strip() == 'System: -1' or answer == '/n-1' or answer.strip() == '/nSystem: -1':
            return {"answer": "he question is not related to the context or could not be answered."}
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
