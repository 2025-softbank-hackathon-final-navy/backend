import os, uvicorn, asyncio
from fastapi import FastAPI
from api import main
from starlette.middleware.cors import CORSMiddleware
from workers.execution_worker import worker_loop

app = FastAPI(root_path="/api")

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main.api_router)

WORKER_TYPE = os.getenv("WORKER_TYPE")

@app.on_event("startup")
async def startup_event():
    use_gpu = (WORKER_TYPE == "gpu")
    print(f"Starting FastAPI app as a {WORKER_TYPE.upper()} worker.")
    asyncio.create_task(worker_loop(use_gpu=use_gpu))

@app.get("/")
def read_root():
    return {"Hello": "World"}