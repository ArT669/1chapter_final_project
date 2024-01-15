from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func

from table_user import User
from table_post import Post
from table_feed import Feed
from database import SessionLocal
from schema import UserGet, PostGet, FeedGet

def get_db():
    with SessionLocal() as db:
        return db

app = FastAPI()

"""Валидация и ответ сервера на запрос конкретного юзера"""
@app.get("/user/{id}", response_model=UserGet)

async def select_user(id : int, db: Session = Depends(get_db)):
    """
    Обрабатывает запрос по id и выводит всю информацию
    или ничего, если пользователя не существует
    """

    result = db.query(User).filter_by(id = id).one_or_none()

    if not result:
        raise HTTPException(status_code = 404, detail = "user not found")
    else:
        return result
    
"""Валидация и ответ сервера на запрос конкретного поста"""
@app.get("/post/{id}", response_model=PostGet)

async def select_post(id : int, db: Session = Depends(get_db)):
    """
    Обрабатывает запрос по id и выводит всю информацию
    или ничего, если поста не существует
    """
    result = db.query(Post).filter_by(id = id).one_or_none()

    if not result:
        raise HTTPException(status_code = 404, detail = "post not found")
    else:
        return result

"""Валидация и ответ сервера на запрос всех действий, проведенных человеком на стене"""
@app.get("/user/{id}/feed", response_model=List[FeedGet])

async def get_user_feed(id : int, limit : int = 10, db: Session = Depends(get_db)):
    """
    Обрабатывает запрос по id пользователя и выводит всю его активность (по лимиту)
    """
    result = db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit)

    if not result:
        raise HTTPException(status_code = 200, details = "")
    return result.all()

"""Валидация и ответ сервера на запрос всех действий, проведенных с постом со стены"""
@app.get("/post/{id}/feed", response_model=List[FeedGet])

async def get_post_feed(id : int, limit : int = 10, db : Session = Depends(get_db)):
    """
    Обрабатывает запрос по id поста и выводит всю его активность (по лимиту)
    """
    result = db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit)

    if not result:
        raise HTTPException(status_code = 200, detail = "")
    else:
        return result.all()
    

"""Часть финального проекта"""
"""
Шпаргалка для SQL запроса
SELECT 
    f.post_id, COUNT(f.post_id)
FROM 
    feed_action f
WHERE 
    f.action = 'like'
GROUP BY 
    f.post_id
ORDER BY 
    COUNT(f.post_id) DESC
LIMIT 10
"""
@app.get("/post/recommendations/", response_model=List[PostGet])

async def get_recommended_feed(id : int = 205, limit : int = 10, db : Session = Depends(get_db)):
    """Топ постов по количеству лайков"""
    result = db.query(Post).select_from(Feed).filter(Feed.action == "like").join(Post, Feed.post_id == Post.id).group_by(Post.id).order_by(func.count(Post.id).desc()).limit(limit).all()

    return result