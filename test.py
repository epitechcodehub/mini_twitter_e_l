from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
"""
class Comment :
    def __init__(self, user, content):
        self.user = user
        self.content = content

    def __str__(self):
        return self.user + " commented : '" + self.content + "'."

class Post :
    def __init__(self, content):
        self.content = content
        self.comments = []
    
    def comment(self, user, comm_content):
        self.comments.append(Comment(user, comm_content));
"""

class Comment(BaseModel):
    comm_id : int
    content : str

class Post(BaseModel) :
    post_id : int
    content : str
    img : str
    user : str
    comments : list

@app.get("/")
async def root():
    posts = []
# return {"posts" : posts}
    return {"Message" : "Hello world"}

@app.get("/posts/create_post")
async def create_post(post_id : int, post : Post):
    return post

@app.get("/posts/create_comment")
async def create_post(comment_id : int, comment : Comment):
    return comment
#@app.get("/posts/{post_id}")
#async def list_post_id(post_id : int, post : Post):
    
