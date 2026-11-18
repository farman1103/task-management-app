from fastapi import FastAPI
from utils.db import Base, engine
from tasks.router import task_router

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management App", description="A simple task management application built with FastAPI.", version="1.0.0")
app.include_router(task_router)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}