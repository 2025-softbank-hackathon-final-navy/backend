from pydantic import BaseModel
from typing import List, Optional

class ExecutionRequest(BaseModel):
    request_id: str
    python_version: str
    dependencies: List[str] = [] # pip install 할 라이브러리 목록
    code: str # 실행할 Python 코드
    timeout: int = 30 # 초 단위
    use_gpu: bool = False # GPU 사용 여부

class ExecutionResult(BaseModel):
    request_id: str
    status: str # "success", "error", "timeout"
    stdout: str
    stderr: str
    duration: float # 실행 시간 (초)
    error_message: Optional[str] = None # 에러 발생 시 메시지
    # memory_usage: Optional[float] = None # (심화)
    # cpu_usage: Optional[float] = None # (심화)
