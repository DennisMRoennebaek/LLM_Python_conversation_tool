from __future__ import annotations

from .config import load_config
from .audio_io import record_wav_push_to_talk, play_wav
from .stt_whisper import WhisperSTT
from .llm_ollama import OllamaLLM
from .tts_piper import PiperTTS


def main() -> None:
    cfg = load_config()

    stt = WhisperSTT()
    llm = OllamaLLM()
    tts = PiperTTS()

    while True:
        try:
            # 1) Record
            record_wav_push_to_talk(cfg.mic_wav)

            # 2) STT
            user_text = stt.transcribe_file(str(cfg.mic_wav))
            print(f"\nYou: {user_text}")

            if not user_text:
                print("Heard nothing — try again.\n")
                continue

            # 3) LLM
            assistant_text = llm.generate(user_text)
            print(f"\nAssistant: {assistant_text}")

            # 4) TTS
            tts.synthesize_to_wav(assistant_text, cfg.tts_wav)

            # 5) Play
            play_wav(cfg.tts_wav)

            print("\n--- (Ctrl+C to quit) ---\n")

        except KeyboardInterrupt:
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
