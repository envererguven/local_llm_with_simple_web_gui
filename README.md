first install ollama 

#curl -fsSL https://ollama.com/install.sh | sh

run ollama
#ollama serve &

#ps aux | grep ollama

pull a model
#ollama pull llama3.2:1b

run it
#ollama run llama3.2:1b

test model:
#curl -X POST http://127.0.0.1:11434/api/generate -H "Content-Type: application/json" -d '{"model": "llama3.2:1b", "prompt": "hello"}'

install app requiremnents
#pip install flask requests

run
#python3 ollama_llm_api.py

connect to the link (on gitpod)
#gp port 5000
