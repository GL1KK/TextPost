from fastapi import FastAPI
import uvicorn
from create_db import create_db
import asyncio
from routers.auth import AuthRouter


app = FastAPI()
auth_router = AuthRouter()
app.include_router(auth_router.router)
@app.on_event("startup")
async def startup():
    await create_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)