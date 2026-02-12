from __future__ import annotations

from faster_whisper import WhisperModel

from .config import load_config


class WhisperSTT:

    def __init__(self) -> None:
        cfg = load_config()

        print("Loading Whisper model... (first time may take a while)")

        self.model = WhisperModel(
            model_size_or_path="small",
            device="cpu",
            compute_type="int8"
        )

        print("Whisper ready.")

    def transcribe_file(self, wav_path: str) -> str:
        segments, info = self.model.transcribe(
            wav_path,
            vad_filter=True, # ignores silence
            language="en"
        )

        text = "".join(segment.text for segment in segments).strip()
        return text
