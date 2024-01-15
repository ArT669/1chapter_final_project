from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func

class User(Base):
    """Оборачивает БД user в ORM"""
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    exp_group = Column(Integer)
    gender = Column(Integer)
    os = Column(String)
    source = Column(String)

if __name__ == "__main__":
    
    # открываю сессию
    session = SessionLocal()

# sql шпаргалка по запросу ниже:
# SELECT
#   country,
#   os,
#   COUNT(*)
# FROM
#   "user"
# WHERE
#   exp_group = 3
# GROUP BY
#   country,
#   os 
# HAVING
#   COUNT(*) > 100
# ORDER BY
#   COUNT(*) DESC

    print(session.query(User.country, User.os, func.count()) # 3 колонки беру в очередь
                 .filter_by(exp_group = 3) # фильтрую по экспериментальной группе == 3
                 .group_by(User.country, User.os) # группирую по стране и ОС
                 .having(func.count() > 100) # having с функциями используется, беру фильтр по значению функции
                 .order_by(func.count().desc()) # фильтрую в порядке убывания
                #  .limit(10) здесь можно поставить лимит
                 .all()) # превращаю все это в список