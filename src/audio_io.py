from __future__ import annotations

import wave
from pathlib import Path

import numpy as np
import sounddevice as sd
import soundfile as sf

from .config import load_config


def record_wav_push_to_talk(out_path: Path) -> None:
    
    cfg = load_config()

    # Allow selecting a specific input device via config (.env)
    # Set AUDIO_INPUT_DEVICE to either an integer index (e.g. "3") or a device name.
    input_device_raw = getattr(cfg, "audio_input_device", "").strip()

    if input_device_raw == "":
        input_device = None
    else:
        # If it's numeric, use int index; otherwise treat it as a device name string.
        input_device = int(input_device_raw) if input_device_raw.isdigit() else input_device_raw

    input("Press Enter to START recording...")
    print("Recording... Press Enter to STOP.")

    if input_device is not None:
        print(f"Using input device: {input_device}")

    chunks: list[np.ndarray] = []

    def callback(indata, frames, time_info, status) -> None:
        if status:
            print(status)
        chunks.append(indata.copy())

    with sd.InputStream(
        samplerate=cfg.sample_rate,
        channels=cfg.channels,
        dtype="int16",
        device=input_device,
        callback=callback,
    ):
        input()  # Wait for user to press Enter to stop recording

    if not chunks:
        raise RuntimeError("No audio captured. Is your microphone working / selected?")

    audio = np.concatenate(chunks, axis=0)

    # Simple sanity check: if it's extremely short, warn
    if audio.shape[0] < cfg.sample_rate // 4:
        print("Warning: very short recording captured.")

    # Write WAV (PCM 16-bit)
    with wave.open(str(out_path), "wb") as wf:
        wf.setnchannels(cfg.channels)
        wf.setsampwidth(2)  # int16 = 2 bytes
        wf.setframerate(cfg.sample_rate)
        wf.writeframes(audio.tobytes())

    print(f"Saved recording: {out_path}")


def play_wav(wav_path: Path) -> None:
    audio, sr = sf.read(str(wav_path), dtype="float32")
    sd.play(audio, sr)
    sd.wait()
