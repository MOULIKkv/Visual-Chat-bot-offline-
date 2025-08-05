# We are switching to the ctransformers library, which is more stable for this hardware.
from ctransformers import AutoModelForCausalLM
# We'll use the huggingface_hub library to handle the download reliably.
from huggingface_hub import hf_hub_download

# --- 1. Check for GPU and set the number of layers to offload ---
# For an RTX 3050 with 4GB VRAM, offloading 15-20 layers is a good starting point.
# If you get errors, try reducing this number. If it's fast, you can try increasing it.
GPU_LAYERS = 20
print(f"✅ Attempting to offload {GPU_LAYERS} layers to the GPU.")

# --- 2. Reliably download the GGUF model ---
# This uses a more robust downloader to prevent the loop issue.
# It will download the file once and then use the local cache.
print("Checking for model... (This will download a few GB the first time)")
model_repo = "TheBloke/zephyr-7B-beta-GGUF"
model_filename = "zephyr-7b-beta.Q4_K_M.gguf"

# hf_hub_download returns the local path to the file
local_model_path = hf_hub_download(repo_id=model_repo, filename=model_filename)
print(f"✅ Model found at: {local_model_path}")

# --- 3. Load the GGUF model from the local path ---
print("Loading model...")
llm = AutoModelForCausalLM.from_pretrained(
    local_model_path,  # We now use the direct local path
    model_type="mistral",
    gpu_layers=GPU_LAYERS,
)
print("✅ Model loaded successfully!")

# --- 4. Start the conversation loop ---
print("\n--- AI Avatar is Ready ---")
print("Ask me anything! Type 'quit' to exit.")

while True:
    user_prompt = input("You: ")
    if user_prompt.lower() == 'quit':
        break

    # The prompt format for this model is slightly different
    full_prompt = f"<|system|>\n</s>\n<|user|>\n{user_prompt}</s>\n<|assistant|>\n"

    print("AI is thinking...")

    # --- 5. Generate the response ---
    response = llm(
        full_prompt,
        max_new_tokens=150,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2  # Helps prevent the model from repeating itself
    )

    print(f"AI: {response}")

print("--- Conversation Ended ---")
