from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database_setup import get_db, SessionLocal
from models import Post, PostModel, list_to_str, str_to_list

app = FastAPI()


@app.get("/", response_model=List[PostModel])
async def index(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    # Convert tags from string to list for each post before returning
    return [PostModel(
        title=post.title,
        content=post.content,
        tags=str_to_list(post.tags)
    ) for post in posts]


@app.post("/post", status_code=status.HTTP_201_CREATED, response_model=PostModel)
async def create_post(post: PostModel, db: Session = Depends(get_db)):
    new_post = Post(
        title=post.title,
        content=post.content,
        tags=list_to_str(post.tags),  # Convert list to string for storage
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    # Convert the tags back to a list before returning
    return PostModel(
        title=new_post.title,
        content=new_post.content,
        tags=str_to_list(new_post.tags)
    )


@app.get("/posts/{post_id}", response_model=PostModel)
async def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    # Convert tags from string to list before returning
    return PostModel(
        title=post.title,
        content=post.content,
        tags=str_to_list(post.tags)
    )


@app.put("/post/{id}", response_model=PostModel)
async def update_post(id: int, post: PostModel, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Update fields including handling tag conversion
    db_post.title = post.title
    db_post.content = post.content
    db_post.tags = list_to_str(post.tags)  # Convert list to string for storage

    db.commit()
    db.refresh(db_post)
    # Convert the tags back to a list before returning
    return PostModel(
        title=db_post.title,
        content=db_post.content,
        tags=str_to_list(db_post.tags)
    )


@app.delete("/post/{id}")
async def delete_post(id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(db_post)
    db.commit()  # Ensure the commit after deleting
    return {"message": "Post deleted successfully"}


@app.get("/posts/tags/{tags}", response_model=List[PostModel])
async def get_posts_by_tag(tags: str, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.tags.contains(tags)).all()
    # Convert tags from string to list for each post before returning
    return [PostModel(
        title=post.title,
        content=post.content,
        tags=str_to_list(post.tags)
    ) for post in posts]
