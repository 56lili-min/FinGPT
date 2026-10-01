# FinGPT-master 项目进度快照
# 创建时间: 2026-09-27
# Python 版本: 3.12
# 虚拟环境: .venv

# ========== 1. 项目根目录路径 ==========
# E:\fingpt\FinGPT-master
# 虚拟环境: E:\fingpt\FinGPT-master\.venv
# 缓存目录: E:\fingpt_cache\  (HuggingFace/Torch/Transformers/Temp 全部在此)

# ========== 2. 已完成并跑通的脚本 ==========
# ✅ cloud_test_fingpt.py  — 依赖检测 & CUDA 检测  [已成功]
# ✅ test_imports.py        — FinBERT 情感分析推理   [已成功, 模型缓存到 E:\fingpt_cache\]
# ✅ explore_more.py        — 量化财报 + 行情API探测 + 情感融合  [已创建, 待跑]

# ========== 3. 运行命令速查 ==========
# 先切到项目目录, 再运行:
#   cd E:\fingpt\FinGPT-master
#   .\.venv\Scripts\python.exe cloud_test_fingpt.py     # 环境检测
#   .\.venv\Scripts\python.exe test_imports.py           # 情感分析
#   .\.venv\Scripts\python.exe explore_more.py            # 进一步探索

# ========== 4. 已验证的依赖版本 ==========
# torch              2.14.0+cpu
# transformers       4.39.3
# peft               0.11.1
# datasets           5.0.1
# accelerate         1.15.0
# sentencepiece      0.2.2
# numpy              1.26.4
# pandas             3.0.6
# yfinance           1.7.0
# tushare            1.4.29
# gradio             6.28.0
# bitsandbytes       NOT INSTALLED  (GPU量化专用, CPU不需要)

# ========== 5. HuggingFace 缓存 ==========
# 环境变量硬编码在每个脚本开头:
#   HF_HOME = E:\fingpt_cache\huggingface
#   TRANSFORMERS_CACHE = E:\fingpt_cache\transformers
#   TORCH_HOME = E:\fingpt_cache\torch
#   TEMP/TMP = E:\fingpt_cache\temp
#   HF_ENDPOINT = https://hf-mirror.com  (国内镜像, 解决被墙问题)
# 已缓存模型: ProsusAI/finbert (~400MB, 存在 E:\fingpt_cache\huggingface\)

# ========== 6. 已知问题 & 解决方案 ==========
# ❶ yfinance 在国内被 Yahoo 限流
#   → 解决: 推荐安装 AKShare (pip install akshare), 免token, 覆盖A股/港股/美股/期货
#   → 或: 脚本已内置 UA 伪装 + 3秒间隔 + 3次重试
#
# ❷ bitsandbytes 未安装
#   → CPU 推理不需要它, 仅 GPU 量化训练时需要
#
# ❸ ProsusAI/finbert 是英文模型, 中文情感识别不准 (结果全是中性)
#   → 解决: 换中文金融情感模型, 如 ckiplab/bert-base-chinese-financial

# ========== 7. 下一步可探索方向 ==========
# ① 安装 AKShare 获取真实A股行情:  .\.venv\Scripts\pip.exe install akshare
# ② 换中文金融情感模型, 让结果更准
# ③ 跑 Llama2 + FinGPT LoRA (需要 8GB+ GPU 显存)
# ④ 接入 Tushare A股数据 (需注册 token: https://tushare.pro)

# ========== 8. 缓存目录结构 ==========
# E:\fingpt_cache\
# ├── huggingface\     ← 模型文件 (finbert ~400MB)
# ├── transformers\    ← transformers 缓存
# ├── torch\           ← PyTorch 权重
# ├── temp\            ← 临时文件
# └── pip\             ← pip 缓存

# ========== 9. pip 安装命令模板 ==========
# .\.venv\Scripts\pip.exe install <包名>
# .\.venv\Scripts\pip.exe install akshare              # 行情API
# .\.venv\Scripts\pip.exe install -r requirements.txt  # 批量安装