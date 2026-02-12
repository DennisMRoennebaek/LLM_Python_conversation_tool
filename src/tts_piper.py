from __future__ import annotations

import subprocess
from pathlib import Path

from .config import load_config


class PiperTTS:
    
    def __init__(self) -> None:
        cfg = load_config()
        self.exe = cfg.piper_exe
        self.voice = cfg.piper_voice_path

        if not self.exe.exists():
            raise FileNotFoundError(f"Piper exe not found: {self.exe}")
        if not self.voice.exists():
            raise FileNotFoundError(f"Piper voice not found: {self.voice}")

    def synthesize_to_wav(self, text: str, wav_out: Path) -> None:
        cmd = [str(self.exe), "-m", str(self.voice), "-f", str(wav_out)]

        result = subprocess.run(
            cmd,
            input=text.encode("utf-8"),
            capture_output=True,
        )

        if result.returncode != 0:
            stderr = result.stderr.decode("utf-8", errors="ignore")
            raise RuntimeError(f"Piper failed:\n{stderr}")
