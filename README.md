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

System Requirements
Minimum Requirements:
Operating System: Windows 10/11 (64-bit)

GPU: An NVIDIA GPU with at least 4 GB of VRAM and CUDA support. An NVIDIA GeForce RTX 3050 (Laptop or Desktop) is a good baseline.

CPU: A modern processor with at least 4 cores.

RAM: 16 GB of system RAM.

Storage: Approximately 20 GB of free disk space for the development environment and the downloaded AI models.

Recommended Requirements:
GPU: An NVIDIA GPU with 8 GB or more of VRAM (e.g., RTX 3060, 4060, or higher) for better performance and the ability to run larger models.

RAM: 32 GB of system RAM.

Storage: A fast SSD for quicker model loading times.

Installation and Setup
Follow these steps to get the project running on your local machine.

Step 1: Install Prerequisites
Before you begin, ensure you have the necessary software installed.

NVIDIA Drivers: Make sure you have the latest NVIDIA Game Ready or Studio drivers installed. You can download them from the NVIDIA website.

Python: Install Python 3.10 or 3.11. You can download it from the official Python website. Important: During installation, make sure to check the box that says "Add Python to PATH".

Git: Install Git for version control. Download it from git-scm.com.

Step 2: Clone the Repository
Open a command prompt (CMD) or PowerShell and use Git to clone your repository. Replace YOUR_USERNAME with your actual GitHub username.

Bash

git clone https://github.com/YOUR_USERNAME/local-ai-avatar.git
cd local-ai-avatar
Step 3: Create a Python Virtual Environment
It's best practice to create an isolated environment for the project's dependencies.

Bash

# Create a virtual environment named ".venv"
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\activate
You will know it's active when you see (.venv) at the beginning of your command prompt line.

Step 4: Install Required Libraries
Now, install the necessary Python libraries using pip. This command specifically installs the ctransformers library with CUDA support, which is crucial for GPU acceleration.

Bash

pip install "ctransformers[cuda]>=0.2.27"
Step 5: Run the Application
You are now ready to run the AI. Execute the main script:

Bash

python run_local_llm.py
Note: The very first time you run this command, it will download the AI model file (approximately 4.4 GB). This may take several minutes depending on your internet connection. Subsequent launches will be much faster as the model will be loaded from your local cache.

Once the model is loaded, you can start chatting with your AI directly in the terminal!
