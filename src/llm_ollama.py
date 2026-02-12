from __future__ import annotations

import requests

from .config import load_config


class OllamaLLM:
    
    def __init__(self) -> None:
        cfg = load_config()
        self.url = cfg.ollama_url
        self.model = cfg.ollama_model

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }
        r = requests.post(self.url, json=payload, timeout=600)
        r.raise_for_status()
        data = r.json()
        return (data.get("response") or "").strip()
