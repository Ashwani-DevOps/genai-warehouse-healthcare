FROM python:3.10-slim
WORKDIR /app
COPY dashboard.py ./dashboard.py
COPY ../src/ ./src/
COPY ../data/ ./data/
COPY ../requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
