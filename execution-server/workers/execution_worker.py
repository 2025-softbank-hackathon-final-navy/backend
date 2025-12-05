import os
import asyncio
import json
import time
from typing import Dict, Any

from utils.queue import pop_job, publish_result
from schemas.execution import ExecutionRequest, ExecutionResult

IMAGE_MAP = {
    "python": "registry/python-runner:3.10",
    "node": "registry/node-runner:18",
    "go": "registry/go-runner:1.22",
    "test": "python:3.10"
}

async def execute_in_docker(request: ExecutionRequest) -> ExecutionResult:
    print(f"Simulating Docker execution for request_id: {request.request_id}")
    start_time = time.time()
    
    runtime = request.runtime.lower()
    #docker_image = IMAGE_MAP[runtime]
    docker_image = IMAGE_MAP.get("test")
    
    end_time = time.time()
    duration = end_time - start_time

    return ExecutionResult(
        request_id=request.request_id,
        status="success",
        stdout=f"Code executed in container [{docker_image}]",
        stderr="",
        duration=duration,
        error_message=None
    )

async def worker_loop(use_gpu: bool):
    worker_name = "GPU" if use_gpu else "CPU"
    print(f"{worker_name} Worker loop started, waiting for jobs...")
    
    while True:
        try:
            _, raw_data = await asyncio.to_thread(pop_job, use_gpu=use_gpu)
            payload = raw_data.decode('utf-8')
            print(f"[{worker_name}] Job received: {payload}")
            
            task_dict = json.loads(payload)
            request = ExecutionRequest(**task_dict)
            result = await execute_in_docker(request)
            
            await asyncio.to_thread(publish_result, result.request_id, result.model_dump_json())
            print(f"[{worker_name}] Result published for request_id: {result.request_id}")

        except json.JSONDecodeError as e:
            print(f"[{worker_name}] JSON decoding error: {e} for data: {payload}")
        except Exception as e:
            print(f"[{worker_name}] Error in worker loop: {e}")
            await asyncio.sleep(5)
