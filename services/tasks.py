from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status
from schemas.task import TaskCreate, TaskResponse, TaskUpdate
from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime, timezone
from utils.datetime import ensure_datetime
from pymongo import ReturnDocument

COLLECTION_NAME = "tasks"

async def create_task(task_in: TaskCreate, db: AsyncIOMotorDatabase):
    now = datetime.now(timezone.utc)
    data = task_in.model_dump()
    data["due_date"] = ensure_datetime(data.get("due_date"))
    data["created_at"] = now
    data["updated_at"] = now
    
    result = await db[COLLECTION_NAME].insert_one(data)
    stored = await db[COLLECTION_NAME].find_one({"_id": result.inserted_id})
    if not stored:
        raise HTTPException(500, "Error inserting task")
    
    stored["id"] = str(stored["_id"])
    stored.pop("_id", None)
    return TaskResponse(**stored)



async def get_all_tasks(db: AsyncIOMotorDatabase):
    tasks = []
    async for task in db[COLLECTION_NAME].find():
        task["id"] = str(task["_id"])
        task.pop("_id", None)
        tasks.append(TaskResponse(**task))
    return tasks


async def get_task_by_id(task_id: str, db: AsyncIOMotorDatabase):
    try:
        task_id = ObjectId(task_id)
        task = await db[COLLECTION_NAME].find_one({"_id": task_id})
    except InvalidId:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid user ID format")

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {task_id} not found")
    task["id"] = str(task["_id"])
    task.pop("_id", None)
    return TaskResponse(**task)


async def update_task(task_id: str, task_in: TaskUpdate, db: AsyncIOMotorDatabase):
    try:
        oid = ObjectId(task_id)
    except InvalidId:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid task ID format")

    data = task_in.model_dump(exclude_unset=True)
    if "due_date" in data:
        data["due_date"] = ensure_datetime(data["due_date"])
    if not data:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No fields provided for update")

    data["updated_at"] = datetime.now(timezone.utc)

    updated = await db[COLLECTION_NAME].find_one_and_update(
        {"_id": oid},
        {"$set": data},
        return_document=ReturnDocument.AFTER
    )
    if not updated:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Task with id {task_id} not found")

    updated["id"] = str(updated["_id"])
    updated.pop("_id", None)
    return TaskResponse(**updated)


async def delete_task(task_id: str, db: AsyncIOMotorDatabase):
    try:
        oid = ObjectId(task_id)
    except InvalidId:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid task ID format")

    result = await db[COLLECTION_NAME].delete_one({"_id": oid})
    if result.deleted_count == 0:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Task with id {task_id} not found")
    
    return {"message": f"Task with id {task_id} deleted successfully"}