"""
Configuration settings for the Telegram bot and Huggingface API,
as well as Redis caching.
Sensitive credentials (TELEGRAM_TOKEN and HF_API_TOKEN) should be stored 
securely in environment variables.
"""

import os

# Telegram Bot Token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")

# Huggingface API Token
HF_API_TOKEN = os.getenv("HF_API_TOKEN", "YOUR_HF_API_TOKEN")

# Huggingface API model endpoints
MODEL_ENDPOINTS = {
    "flux": "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev",
    "stable": "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large",
}

# Fixed prompt parameters to be appended to the user prompt
FIXED_PROMPT_PARAMS = (
    ", clean, high-resolution, 8k, best quality, masterpiece, HDR, UHD, 64K, studio lighting, " +
    "photorealistic, hyper realistic, symmetric face, unreal engine, bokeh, High resolution scan, " +
    "professional photograph, realistic, highly detailed, art-station, trending, realistic face, " +
    "realistic skin, detailed eyes, great artwork, ultra render, lean, golden hour lighting, " +
    "ultra wide angle lens, HDR photography, breathtaking, sharp focus"
)

# Fixed payload structures for the two models.
MODEL_PAYLOADS = {
    "flux": {
        "parameters": {
            "guidance_scale": 3.5,
            "num_inference_steps": 35,
            "width": 768,
            "height": 1334,
            "seed": -1,
        },
        "x-use-cache": False,
        "x-wait-for-model": True
    },
    "stable": {
        "parameters": {
            "guidance_scale": 4.5,
            "num_inference_steps": 45,
            "width": 768,
            "height": 1334,
            "seed": -1,
        },
        "x-use-cache": False,
        "x-wait-for-model": True
    }
}

# Redis cache configuration (open source)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))