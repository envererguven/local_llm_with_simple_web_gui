FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY ollama_llm_api.py . 

COPY ollama_llm.html .

EXPOSE 5000 11434

ENV FLASK_APP=ollama_llm_api.py

CMD bash -c "ollama serve & sleep 5 && ollama pull llama3.2:1b && flask run --host=0.0.0.0 --port=5000"
