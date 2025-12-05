from pydantic import BaseModel
from typing import Dict, Optional

class ExecutionRequest(BaseModel):
    request_id: int
    function_name: str
    runtime: str
    function_code: str
    env_vars: Optional[Dict[str, str]] = None
    use_gpu: bool = False

class ExecutionResult(BaseModel):
    request_id: int
    status: str # "success", "error", "timeout"
    stdout: str
    stderr: str
    duration: float
    error_message: Optional[str] = None 
    # memory_usage: Optional[float] = None 
    # cpu_usage: Optional[float] = None 
