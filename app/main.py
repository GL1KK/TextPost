from fastapi import FastAPI, Depends, Header, HTTPException, Request
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
import uvicorn
from routers.auth import AuthRouter
from routers.users import UserRouter
from routers.posts import PostRouter
from create_db import create_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

auth_router = AuthRouter()
user_router = UserRouter()
post_router = PostRouter()
app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(post_router.router)

@app.on_event("startup")
async def startup():
    await create_db()