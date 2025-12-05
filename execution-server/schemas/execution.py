from pydantic import BaseModel
from typing import Dict, Optional, Any

class ExecutionRequest(BaseModel):
    request_id: str
    function_id: str
    runtime: str
    args: Optional[Dict[str, Any]] = None
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
