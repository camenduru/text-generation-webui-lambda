import os
os.system(f"git lfs install")
os.system(f"git clone -b v1.8 https://github.com/camenduru/text-generation-webui /home/demo/source/text-generation-webui")
os.chdir(f"/home/demo/source/text-generation-webui")
os.system(f"pip install -r requirements.txt")

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/Llama-2-13b-chat-hf/resolve/main/model-00001-of-00003.safetensors -d /home/demo/source/text-generation-webui/models/Llama-2-13b-chat-hf -o model-00001-of-00003.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/Llama-2-13b-chat-hf/resolve/main/model-00002-of-00003.safetensors -d /home/demo/source/text-generation-webui/models/Llama-2-13b-chat-hf -o model-00002-of-00003.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/Llama-2-13b-chat-hf/resolve/main/model-00003-of-00003.safetensors -d /home/demo/source/text-generation-webui/models/Llama-2-13b-chat-hf -o model-00003-of-00003.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/Llama-2-13b-chat-hf/raw/main/model.safetensors.index.json -d /home/demo/source/text-generation-webui/models/Llama-2-13b-chat-hf -o model.safetensors.index.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/Llama-2-13b-chat-hf/raw/main/special_tokens_map.json -d /home/demo/source/text-generation-webui/models/Llama-2-13b-chat-hf -o special_tokens_map.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/Llama-2-13b-chat-hf/resolve/main/tokenizer.model -d /home/demo/source/text-generation-webui/models/Llama-2-13b-chat-hf -o tokenizer.model")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/Llama-2-13b-chat-hf/raw/main/tokenizer_config.json -d /home/demo/source/text-generation-webui/models/Llama-2-13b-chat-hf -o tokenizer_config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/Llama-2-13b-chat-hf/raw/main/config.json -d /home/demo/source/text-generation-webui/models/Llama-2-13b-chat-hf -o config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/Llama-2-13b-chat-hf/raw/main/generation_config.json -d /home/demo/source/text-generation-webui/models/Llama-2-13b-chat-hf -o generation_config.json")

os.system(f"python server.py --share --chat --port 8266 --model /home/demo/source/text-generation-webui/models/Llama-2-13b-chat-hf")