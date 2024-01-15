from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)

if __name__ == "__main__":
    # создаю сессию через сессионный мейкер из database.py
    session = SessionLocal()
    # получаю посты через очередь в сессии (похоже на редаш)
    # фильтрую по бизнесу
    # группирую по айди в порядке убывания (DESC)
    # беру 10 штук первых и преобразую с помощью команды all в список!
    posts = session.query(Post).filter_by(topic='business').order_by(Post.id.desc()).limit(10).all()
    
    ids = [post.id for post in posts]
    print(ids)
