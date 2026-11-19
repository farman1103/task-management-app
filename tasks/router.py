from fastapi import APIRouter
from tasks.service import create_task
from tasks.schema import CreateTaskRequest

task_router = APIRouter(prefix="/task", tags=["task"])

@task_router.post("/create")
def create_task_endpoint(request: CreateTaskRequest):
    return create_task(request)




