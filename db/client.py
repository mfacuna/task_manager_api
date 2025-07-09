from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from config.setting import Setting

settings = Setting()
_mongo_client = AsyncIOMotorClient(settings.MONGODB_URI)
_db = _mongo_client[settings.DB_NAME]

async def get_db() -> AsyncIOMotorDatabase:
    return _db