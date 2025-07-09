from fastapi import FastAPI
from routers import tasks

app = FastAPI()


# Routers
app.include_router(tasks.router)


@app.get("/")
async def root():
    return {"message": "This is a Task Management API"}