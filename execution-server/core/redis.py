import os, redis
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

@lru_cache
def get_redis():
    return redis.Redis(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT")),
        decode_responses=True
    )