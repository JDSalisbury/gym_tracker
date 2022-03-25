from fastapi import FastAPI
from .routers import users, gym
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request

app = FastAPI()
app.include_router(users.r, tags=["Users"])
app.include_router(gym.r, tags=["Gym"])
app.add_middleware(SessionMiddleware, secret_key="secret-string")


@app.get("/")
async def root():
    return {"message": "Hello World"}
