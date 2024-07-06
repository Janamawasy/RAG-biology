# PDF QA Agent

This project is a Question-Answering (QA) system built using Retrieval-Augmented Generation (RAG) techniques. It allows users to ask questions based on the content of provided PDFs. The application consists of a backend server using FastAPI and a frontend UI built with Streamlit.

## Features
- Extracts and processes text from PDFs.
- Uses a Vector Store to store and retrieve relevant document chunks.
- Answers questions based on the content of the provided PDFs.
- Displays answers in green and error messages in red in the UI.

## Prerequisites

- Docker
- Python 3.10
- Pip
- Git
- Langchain

## Install Dependencies
Create and activate a virtual environment:

```
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  
  pip install -r requirements.txt
```

## Environment Variables
Create a .env file in the root directory of the project and add your API key and server URL,
api_key for [AI21 embedding mpdel](https://studio.ai21.com/account/api-key?source=docs).

```
  AI21_API_KEY=your_ai21_api_key
  SERVER_URL=http://localhost:8000
```

## Running the Project
### Using Docker
Build and run the Docker container:
```
  docker build -t pdf-qa-agent .
  docker run -p 8000:8000 -p 8501:8501 pdf-qa-agent
```

### Without Docker
Run the FastAPI server:
```
uvicorn server:app --host 0.0.0.0 --port 8000
```
Run the Streamlit UI:
```
streamlit run gui.py --server.port 8501 --server.enableCORS false
```

## Project Structure
```
  ├── data
  │   ├── introduction to cells.pdf
  │   ├── introduction to metabolism - enzymes and energy.pdf
  │   └── the cell cycle and mitosis.pdf
  ├── utils
  │   └── rag_utils.py
  ├── gui.py
  ├── server.py
  ├── rag.py
  ├── requirements.txt
  ├── Dockerfile
  ├── README.md
  └── .env
```

## Explanation of Main Files
  - data/: Folder containing the PDF documents.
  - utils/rag_utils.py: Contains utility functions for extracting text from PDFs.
  - gui.py: Contains the Streamlit UI code.
  - server.py: Contains the FastAPI server code.
  - rag.py: Contains the RAG class with all the logic for document processing, embedding, vectorstore and question answering.
  - requirements.txt: List of dependencies required for the project.
  - Dockerfile: Docker configuration file.
  - README.md: This file, containing project instructions and information.




