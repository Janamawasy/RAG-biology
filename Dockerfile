# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory to the working directory in the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8501 8000

# Command to run both the server and the UI
CMD ["sh", "-c", "streamlit run ui.py & uvicorn server:app --host 0.0.0.0 --port 8000 --reload"]
