from core.redis import get_redis

CPU_REQUEST_QUEUE = "function:queue:cpu"
GPU_REQUEST_QUEUE = "function:queue:gpu"
RESPONSE_CHANNEL = "function:result" 

def pop_job(use_gpu: bool = False):
    redis = get_redis()
    queue = GPU_REQUEST_QUEUE if use_gpu else CPU_REQUEST_QUEUE
    return redis.blpop(queue)

def publish_result(job_id: str, result: str):
    redis = get_redis()
    redis.publish(f"{RESPONSE_CHANNEL}:{job_id}", result)