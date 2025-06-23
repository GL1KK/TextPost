from fastapi import APIRouter, Depends, Request
from services.post_service import PostService, get_post_service
from schemas.posts import PostResponse, PostUpdate
from utils.security import auth

class PostRouter:
    def __init__(self):
        self.router = APIRouter(tags=["Posts"])
        self._setup_routers()

    def _setup_routers(self):
        self.router.post(f"/posts/new_post", response_model=PostResponse)(self.new_post)
        self.router.delete("/posts/delete_post")(self.delete_post)
        self.router.get("/posts/search", response_model=list[PostResponse])(self.get_post_title)
        self.router.patch("/posts/update_post", response_model=PostResponse)(self.update_post)
    
    async def new_post(self, title: str, data: str, depends: str = Depends(auth.access_token_required), post_service: PostService = Depends(get_post_service)):
        #print(depends.sub)
        post = await post_service.new_post(title=title, data=data, user_id=int(depends.sub))
        return post
    async def delete_post(self, post_id: int,depends: str = Depends(auth.access_token_required), post_service: PostService = Depends(get_post_service)):
        post = await post_service.delete_post(post_id=post_id)
        return post
    async def get_post_title(self, title: str, post_service: PostService = Depends(get_post_service)):
        posts = await post_service.get_post_title(title=title)
        return posts
    async def update_post(self, post_id: int, post_update: PostUpdate, post_service: PostService = Depends(get_post_service), depends: str = Depends(auth.access_token_required)):
        post = await post_service.update_post(post_id=post_id, title=post_update.title, data=post_update.data)
        return post