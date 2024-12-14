import uvicorn
from fastapi import FastAPI
from app.routers import task, user
from app.backend.db import engine, Base

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)