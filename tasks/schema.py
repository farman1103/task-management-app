from pydantic import BaseModel

class CreateTaskRequest(BaseModel):
    id: int
    title: str
    description: str
    status: str