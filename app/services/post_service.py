from sqlalchemy.exc import IntegrityError, DBAPIError
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends
from models.posts import Posts
from typing import Optional, Dict, Any
from database import get_db

class PostService: 
    
    def __init__(self, session: AsyncSession):
        self.session = session

    async def new_post(self, title: str, data: str, user_id: int):
        try:
            post = Posts(
                title=title,
                data=data,
                user_id=user_id,
            )
            
            self.session.add(post)
            await self.session.commit()
            await self.session.refresh(post)
            
            return post
            
        except IntegrityError:
            await self.session.rollback()
            raise HTTPException(status_code=400, detail="Invalid data")
        except DBAPIError as e:
            await self.session.rollback()
            raise HTTPException(status_code=500, detail="Database error")
        except Exception as e:
            await self.session.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    async def delete_post(self, post_id: int):
        try:
            query = (
                select(Posts)
                .filter(Posts.id == post_id)
            )
            res = await self.session.execute(query)
            post = res.scalar_one_or_none()
            if not post:
                raise HTTPException(status_code=404, detail="Post not found")

            await self.session.delete(post)
            await self.session.commit()
            
            return {"message": "Post deleted successfully"}
            
        except Exception as e:
            await self.session.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    async def get_post_title(self, title: str) -> list[Posts]:
        query = (
            select(Posts)
            .filter(Posts.title == title)
        )
        res = await self.session.execute(query)
        posts = res.scalars.all()
        return posts
    
async def get_post_service(
    session: AsyncSession = Depends(get_db)
):
    return PostService(session)