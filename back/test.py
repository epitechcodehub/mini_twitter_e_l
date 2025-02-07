from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Base, Post  # Ensure your Post model has matching attributes
from schemas import PostSchema
from database import engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow all origins for development purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def home():
    return {"message": "Wassup gang'"}

@app.post("/createpost")
async def create_post(req: PostSchema, db: Session = Depends(get_db)):
    post = Post(content=req.content, title=req.title, comments=req.comments)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.get("/posts/{title}")
async def get_posts(title: str, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.title == title).first()
    return posts

@app.post("/createcomment/{post_id}")
async def create_comment(post_id: int, comment: str, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.post_id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post.comments.append(comment)
    db.commit()
    db.refresh(post)
    return post

@app.get("/comments/{post_id}")
async def get_comments(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.post_id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post.comments
