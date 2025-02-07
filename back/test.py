from fastapi import FastAPI, Depends, HTTPException
from models import Base, Post
from schemas import PostSchema
from database import engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def home():
    return {"message": "Hello sword!"}

@app.post("/createpost")
async def create_post(req:PostSchema, db: Session = Depends(get_db)):
    post = Post(content=req.content, title=req.title, comments=req.comments)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.get("/posts/{title}")
async def get_posts(title, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.title == title).first()
    return posts
