from database import Base, engine
import asyncio

async def create_db():
    async with engine.begin() as conn: 
        await conn.run_sync(Base.metadata.drop_all)
    async with engine.begin() as conn: 
        await conn.run_sync(Base.metadata.create_all)
    print("ready")

