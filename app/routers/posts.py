from fastapi import APIRouter, Depends, Request
from services.post_service import PostService, get_post_service
from schemas.posts import PostResponse
from utils.security import auth

class PostRouter:
    def __init__(self):
        self.router = APIRouter(tags=["Posts"])
        self._setup_routers()

    def _setup_routers(self):
        self.router.post(f"/posts/new_post", response_model=PostResponse)(self.new_post)
        self.router.delete(f"/posts/delete_post")(self.delete_post)
    
    async def new_post(self, title: str, data: str, depends: str = Depends(auth.access_token_required), post_service: PostService = Depends(get_post_service)):
        #print(depends.sub)
        post = await post_service.new_post(title=title, data=data, user_id=int(depends.sub))
        return post
    async def delete_post(self, post_id: int,depends: str = Depends(auth.access_token_required), post_service: PostService = Depends(get_post_service)):
        post = await post_service.delete_post(post_id=post_id)
        return post