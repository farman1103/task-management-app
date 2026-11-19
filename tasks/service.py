from tasks.schema import CreateTaskRequest
from utils.db import get_db
from tasks.models import TaskModel

def create_task(request: CreateTaskRequest):
    # Implementation for creating a task in the postgres database 
    db = next(get_db())  # Get a database session
    new_task = TaskModel(
        id=request.id,
        title=request.title,
        description=request.description,
        status=request.status
    )
    db.add(new_task)
    if request.id in db.query(TaskModel.id).filter(TaskModel.id == request.id).all():
        return {"status": "Task with this ID already exists!"}
    db.commit()
    db.refresh(new_task)
    db.close()  # Close the database session 
    return {"status": "Task created successfully!"}