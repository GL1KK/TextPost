from fastapi import APIRouter, Depends, Request
from services.post_service import PostServies
from schemas.posts import PostResponse
from utils.security import auth

class PostRouter:
    def __init__(self):
        self.router = APIRouter(tags=["Posts"])
        self.__post_servies = PostServies()
        self._setup_routers()

    def _setup_routers(self):
        self.router.post(f"/posts/new_post", response_model=PostResponse)(self.new_post)
        self.router.delete(f"/posts/delete_post")(self.delete_post)
    
    async def new_post(self, title: str, data: str, depends: str = Depends(auth.access_token_required)):
        #print(depends.sub)
        post = await self.__post_servies.new_post(title=title, data=data, user_id=int(depends.sub))
        return post
    async def delete_post(self, post_id: int,depends: str = Depends(auth.access_token_required)):
        post = await self.__post_servies.delete_post(post_id=post_id)
        return post