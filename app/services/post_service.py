from models.posts import Posts
from .user_service import UserServies
from sqlalchemy.exc import IntegrityError, DBAPIError
from sqlalchemy import text, select, and_, cast, delete
from sqlalchemy.orm import selectinload, joinedload
from datetime import datetime
from database import Base, engine, session
from utils.security import Security, config
from fastapi import HTTPException, Response

class PostServies:
    
    def __init__(self):
        self.__user_servies = UserServies()

    async def new_post(self, title: str ,data: str, user_id: int):
        async with session() as sn:
            try:
                post = Posts(
                    title=title,
                    data=data,
                    user_id=user_id,
                )
                user = await self.__user_servies.get_profile(user_id=str(user_id))
                sn.add(post)
                await sn.commit()
                await sn.refresh(post)
                return post
            except Exception as e:
                return str(e)
    
    async def delete_post(self, post_id: int):
        async with session() as sn:
            try:
                query = (
                    select(Posts)
                    .filter(Posts.id == post_id)
                )
                res = await sn.execute(query)
                post = res.scalars().first()
                if not post:
                    raise HTTPException(status_code=404, detail="Post not found!")

                await sn.delete(post)
                await sn.commit()
                return{
                    "Message": "Deleted!"
                }
            except Exception as e:
                await sn.rollback()
                return str(e)