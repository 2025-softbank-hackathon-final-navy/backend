from core.redis import get_redis

REQUEST_QUEUE = "jobs:request" 
RESPONSE_QUEUE = "jobs:response:"

def push_job(job_id: str, result: str):
    redis = get_redis()
    redis.rpush(f"{RESPONSE_QUEUE}{job_id}", result)

def pop_job():
    redis = get_redis()
    return redis.blpop(REQUEST_QUEUE)