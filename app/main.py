from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID
from typing import List
from datetime import timedelta

import app.crud as crud
import app.schemas as schemas
import app.database as database
from app.auth import verify_token, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI(    
    title="ToDo API",
    description="ToDo API for task management",
    version="1.0.0",
    docs_url="/docs",  # URL for Swagger UI
    redoc_url="/redoc",  # URL for ReDoc
    )

@app.on_event("startup")
async def startup_event():
    print("Starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")

# API to GET access token
@app.get("/token", summary="Get access token")
async def get_access_token():
    """
    returns access token
    """
    data = {"sub": "testuser"}
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data=data, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

# API endpoints
@app.post("/tasks/create", response_model=schemas.Task, dependencies=[Depends(verify_token)], summary="creates new task")
async def create_task(task_data: schemas.TaskBase, db: AsyncSession = Depends(database.get_db)):
    """
    Creates a new task with the specified data

    - **task_data**: task data in JSON format (includes `datetime_to_do` and `task_info`)
    """
    return await crud.create_task(db=db, task_data=task_data)

@app.get("/tasks/list", response_model=List[schemas.TaskBase], dependencies=[Depends(verify_token)], summary="get list of all tasks")
async def list_tasks(db: AsyncSession = Depends(database.get_db)):
    """
    returns list of all tasks
    """
    return await crud.get_tasks(db=db)

@app.get("/tasks/{task_id}", response_model=schemas.TaskBase, dependencies=[Depends(verify_token)], summary="get task by ID")
async def get_task(task_id: UUID, db: AsyncSession = Depends(database.get_db)):
    """
    returns task by ID

    - **task_id**: UUID
    """
    return await crud.get_task(db=db, task_id=task_id)

@app.patch("/tasks/{task_id}/update", response_model=schemas.Task, dependencies=[Depends(verify_token)], summary="update task by ID")
async def update_task(task_id: UUID, task_data: schemas.PartialUpdateTask,  db: AsyncSession = Depends(database.get_db)):
    """
    Updates task by ID

    - **task_id**: UUID
    - **task_data**: new data for the task
    """
    return await crud.update_task(db=db, task_id=task_id, task_data=task_data)


