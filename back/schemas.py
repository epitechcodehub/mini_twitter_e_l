from pydantic import BaseModel

class PostSchema(BaseModel):
    post_id : int
    content : str
    title : str
    comments : list[str]
