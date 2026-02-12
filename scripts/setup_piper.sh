#!/usr/bin/env bash

set -e

echo "Installing Piper TTS..."

mkdir -p runtime/piper
mkdir -p runtime/piper/voices

cd runtime/piper

# -----------------------------
# Download Piper binary
# -----------------------------
if [ ! -f "piper.exe" ]; then
  echo "Downloading Piper..."

  curl -L -o piper.zip \
    https://github.com/rhasspy/piper/releases/latest/download/piper_windows_amd64.zip

  unzip piper.zip
  rm piper.zip

  echo "Piper installed."
else
  echo "Piper already exists."
fi

# -----------------------------
# Download default voice
# Change the variables below to download a different voice
# -----------------------------
cd voices

LANGUAGE="en_US"
CADENCE="medium"
NAME="amy"

VOICE="${LANGUAGE}-${NAME}-${CADENCE}"

if [ ! -f "${VOICE}.onnx" ]; then
  echo "Downloading voice: ${VOICE}..."

  curl -L -o ${VOICE}.onnx \
    https://huggingface.co/rhasspy/piper-voices/resolve/main/en/${LANGUAGE}/${NAME}/${CADENCE}/${VOICE}.onnx

  curl -L -o ${VOICE}.onnx.json \
    https://huggingface.co/rhasspy/piper-voices/resolve/main/en/${LANGUAGE}/${NAME}/${CADENCE}/${VOICE}.onnx.json

  echo "Voice installed."
else
  echo "Voice already exists."
fi

echo "Piper setup finished."
