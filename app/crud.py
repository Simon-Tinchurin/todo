from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from fastapi import HTTPException

from uuid import UUID, uuid4
from datetime import datetime

from . import schemas, models

async def create_task(db: AsyncSession, task_data: schemas.TaskBase):
    task = models.Task(
        id=uuid4(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        datetime_to_do=task_data.datetime_to_do,
        task_info=task_data.task_info
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_task(db: AsyncSession, task_id: UUID):
    result = await db.execute(select(models.Task).filter(models.Task.id == task_id))
    task = result.scalars().first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return schemas.TaskBase.model_validate(task)

async def get_tasks(db: AsyncSession):
    result = await db.execute(select(models.Task))
    tasks = result.scalars().all()
    return [schemas.TaskBase.model_validate(task) for task in tasks]

async def update_task(db: AsyncSession, task_id: UUID, task_data: schemas.PartialUpdateTask):
    result = await db.execute(select(models.Task).filter(models.Task.id == task_id))
    task = result.scalars().first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    if task_data.datetime_to_do is not None:
        task.datetime_to_do = task_data.datetime_to_do
    if task_data.task_info is not None:
        task.task_info = task_data.task_info

    task.updated_at = datetime.now()

    await db.commit()
    await db.refresh(task)
    return task


