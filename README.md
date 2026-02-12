# Speak2Me

Speak2Me is a local voice assistant that runs entirely on your machine.

It records your voice, transcribes it with Whisper, sends it to a local
LLM (Ollama), and speaks the response using Piper.

## Run locally

### 1) Clone repo

git clone https://github.com/yourusername/speak2me cd speak2me

### 2) Setup environment

bash scripts/setup.sh

### 3) Install and start Ollama

ollama pull llama3.1:8b ollama serve

### 4) Configure

cp .env.example .env

### 5) Run

source .venv/Scripts/activate python -m src.main

Press Enter to record, press Enter again to stop. The assistant will
respond with voice.
