import os
import sys

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["HF_HOME"] = "E:/fingpt_cache/huggingface"
os.environ["HUGGINGFACE_HUB_CACHE"] = "E:/fingpt_cache/huggingface/hub"
os.environ["TRANSFORMERS_CACHE"] = "E:/fingpt_cache/transformers"
os.environ["TORCH_HOME"] = "E:/fingpt_cache/torch"
os.environ["TEMP"] = "E:/fingpt_cache/temp"
os.environ["TMP"] = "E:/fingpt_cache/temp"

print("=" * 60)
print("FinGPT 金融情感分析")
print("=" * 60)
print(f"镜像源: {os.environ['HF_ENDPOINT']}")
print(f"缓存目录: {os.environ['HF_HOME']}")
print()

from transformers import pipeline

print("正在加载 FinGPT 轻量级金融情感分析模型...")
print("(首次运行会从国内镜像下载约 400MB 模型)")
classifier = pipeline("sentiment-analysis", model="ProsusAI/finbert")

test_texts = [
    "公司第三季度财报远超预期，股价大涨！",
    "由于供应链问题，利润大幅下降，面临严峻挑战。",
    "该公司的营收符合市场预期。"
]

print("\n--- 分析结果 ---")
for text in test_texts:
    result = classifier(text)[0]
    label_map = {"positive": "积极", "negative": "消极", "neutral": "中性"}
    label = label_map.get(result['label'].lower(), result['label'])
    print(f"原文: {text}")
    print(f"情感: {label} (置信度: {result['score']:.2f})\n")

print("=" * 60)
print("全部完成!")
print("=" * 60)