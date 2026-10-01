import os, sys, subprocess

CACHE = "E:/fingpt_cache"
for d in [f"{CACHE}/huggingface", f"{CACHE}/huggingface/hub",
          f"{CACHE}/torch", f"{CACHE}/transformers", f"{CACHE}/temp", f"{CACHE}/pip"]:
    os.makedirs(d, exist_ok=True)

for k, v in {
    "HF_HOME": f"{CACHE}/huggingface",
    "HUGGINGFACE_HUB_CACHE": f"{CACHE}/huggingface/hub",
    "TRANSFORMERS_CACHE": f"{CACHE}/transformers",
    "TORCH_HOME": f"{CACHE}/torch",
    "TORCH_EXTENSIONS_DIR": f"{CACHE}/torch/extensions",
    "TEMP": f"{CACHE}/temp",
    "TMP": f"{CACHE}/temp",
    "PIP_CACHE_DIR": f"{CACHE}/pip",
}.items():
    os.environ[k] = v

py = ".venv/Scripts/python.exe"

print("=" * 60)
print("[1/2] cloud_test_fingpt.py - 依赖 & CUDA 检测")
print("=" * 60)
subprocess.run([py, "cloud_test_fingpt.py"], cwd=".", env=os.environ, check=False)

print()
print("=" * 60)
print("[2/2] test_imports.py - 金融情感分析推理")
print("=" * 60)
subprocess.run([py, "test_imports.py"], cwd=".", env=os.environ, check=False)

print()
print("=" * 60)
print("全部运行完毕! 缓存位置:", CACHE)
print("=" * 60)