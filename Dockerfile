FROM python:3.12

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000
EXPOSE 8501

CMD ["sh", "-c", "streamlit run ui.py & uvicorn server:app --host 127.0.0.1 --port 8000 --reload"]