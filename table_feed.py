from database import Base, SessionLocal
from table_user import User
from table_post import Post
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

class Feed(Base):
    """Оборачивает feed_action в ORM"""
    __tablename__ = "feed_action"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"), primary_key=True)
    action = Column(String)
    time = Column(DateTime)
    user = relationship(User)
    post = relationship(Post)

