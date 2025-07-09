from fastapi import APIRouter, status, Depends
from schemas.task import TaskCreate, TaskResponse, TaskUpdate
from typing import Annotated
from db.client import get_db
from motor.motor_asyncio import AsyncIOMotorDatabase
from services.tasks import create_task, delete_task, get_all_tasks, get_task_by_id, update_task

MongoDBDep = Annotated[AsyncIOMotorDatabase, Depends(get_db)]

router = APIRouter(prefix="/tasks",tags=["Tasks"], )

# Create a new task
@router.post("/",
            response_model=TaskResponse, 
            status_code=status.HTTP_201_CREATED,
            summary="Create a new task",
             )
async def create_task_route(task_in: TaskCreate, db: MongoDBDep):
    return await create_task(task_in, db)




@router.get("/", 
            response_model=list[TaskResponse], 
            status_code=status.HTTP_200_OK,
            summary="Get all tasks",
    )
async def get_all_tasks_route(db: MongoDBDep):
    return await get_all_tasks(db)
    
    
@router.get("/{id}",
            response_model=TaskResponse, 
            status_code=status.HTTP_200_OK,
            summary="Get a task by ID",
    )
async def get_task_by_id_route(id: str, db: MongoDBDep):
    return await get_task_by_id(id, db)


@router.put("/{id}",
            response_model=TaskResponse, 
            status_code=status.HTTP_200_OK,
            summary="Update a task by ID",
    )
async def update_task_route(id: str, task_in: TaskUpdate, db: MongoDBDep):
    return await update_task(id, task_in, db)



@router.delete("/{id}",
            status_code=status.HTTP_204_NO_CONTENT,
            summary="Delete a task by ID",
    )
async def delete_task_route(id: str, db: MongoDBDep):
    return await delete_task(id, db)



