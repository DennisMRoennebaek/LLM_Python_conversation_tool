from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# Load variables from .env into environment (if .env exists)
load_dotenv()


def env(name: str, default: str) -> str:
    """Read an environment variable with a default."""
    return os.environ.get(name, default)


@dataclass(frozen=True)
class Config:
    # Base folders
    runtime_dir: Path = Path(env("RUNTIME_DIR", "runtime"))

    # Piper
    piper_dir: Path = Path(env("PIPER_DIR", "runtime/piper"))
    piper_exe: Path = Path(env("PIPER_EXE", "runtime/piper/piper.exe"))

    # Voice name must match the actual file name without extension
    # Example: en_US-amy-medium
    piper_voice_name: str = env("PIPER_VOICE", "en_US-amy-medium")

    # Audio
    sample_rate: int = int(env("SAMPLE_RATE", "16000"))
    channels: int = int(env("CHANNELS", "1"))

    # Ollama
    ollama_url: str = env("OLLAMA_URL", "http://localhost:11434/api/generate")
    ollama_model: str = env("OLLAMA_MODEL", "llama3.1:8b")

    # Temp files
    mic_wav: Path = Path(env("MIC_WAV", "mic_in.wav"))
    tts_wav: Path = Path(env("TTS_WAV", "tts_out.wav"))

    @property
    def piper_voice_path(self) -> Path:
        return self.piper_dir / "voices" / f"{self.piper_voice_name}.onnx"

    @property
    def piper_voice_json_path(self) -> Path:
        return self.piper_dir / "voices" / f"{self.piper_voice_name}.onnx.json"


def load_config() -> Config:
    return Config()
