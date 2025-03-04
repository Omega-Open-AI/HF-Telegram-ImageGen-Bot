"""
Asynchronous module to interface with the Huggingface image generation models.
This version uses httpx for asynchronous HTTP calls and integrates basic Redis caching.
"""

import json
import asyncio
import httpx
from config import HF_API_TOKEN, MODEL_ENDPOINTS, MODEL_PAYLOADS, FIXED_PROMPT_PARAMS, REDIS_HOST, REDIS_PORT, REDIS_DB
from monitoring import log_error
import aioredis

# Default headers for requests
HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

# Global variable to store the Redis client.
redis_client = None

async def get_redis_client():
    global redis_client
    if not redis_client:
        redis_client = await aioredis.create_redis_pool((REDIS_HOST, REDIS_PORT), db=REDIS_DB)
    return redis_client

async def generate_image(model: str, prompt: str) -> dict:
    """
    Generic asynchronous function to generate an image using a specified model.
    Applies caching for identical prompts.
    """
    url = MODEL_ENDPOINTS.get(model)
    if not url:
        return {"error": "Model not supported"}
    
    # Create a unique cache key combining model and prompt
    cache_key = f"{model}:{prompt}"
    redis = await get_redis_client()
    cached_response = await redis.get(cache_key)
    if cached_response:
        # Return the cached response if exists
        return json.loads(cached_response.decode("utf-8"))
    
    # Build payload using fixed structure
    payload = MODEL_PAYLOADS[model].copy()
    payload["inputs"] = f"{prompt}{FIXED_PROMPT_PARAMS}"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=HEADERS, json=payload, timeout=60.0)
            response.raise_for_status()
            result = response.json()
            # Cache the result (with a 10 minute TTL)
            await redis.set(cache_key, json.dumps(result), expire=600)
            return result
    except Exception as e:
        log_error(f"{model} model generation failed", e)
        return {"error": str(e)}

async def generate_image_flux(prompt: str) -> dict:
    """
    Generate image using the FLUX model.
    """
    return await generate_image("flux", prompt)

async def generate_image_stable(prompt: str) -> dict:
    """
    Generate image using the Stable Diffusion model.
    """
    return await generate_image("stable", prompt)