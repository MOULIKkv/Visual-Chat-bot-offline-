# Local AI Avatar

This project is an open-source effort to build a fully interactive, conversational AI avatar that runs 100% locally on your personal hardware. The goal is to create an AI companion that is private, customizable, and doesn't rely on cloud APIs.

## 🚀 Features

* **Local Inference:** All AI processing happens on your machine. No data is sent to external servers.
* **GPU Accelerated:** Utilizes your NVIDIA GPU (via CUDA) to run large language models efficiently.
* **Conversational AI:** Chat with a powerful 7-billion-parameter language model in real-time.

## 🛠️ Current Status (August 2025)

The project currently consists of a Python script that successfully:
1.  Loads a GGUF-quantized version of the **Zephyr-7B-beta** model.
2.  Offloads a significant portion of the model to the GPU for fast processing.
3.  Provides a command-line interface for real-time chat with the AI.

##  roadmap

* **Speech-to-Text:** Integrate a local speech recognition model (like Whisper) to talk to the avatar.
* **Text-to-Speech:** Add a local TTS engine to give the avatar a voice.
* **3D Rendering:** Create a real-time 3D avatar that can be animated and lip-synced to the conversation.
