from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    MONGODB_URI: str
    DB_NAME: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
settings = Setting()