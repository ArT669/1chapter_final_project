from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml"

"""Инструмент для работы с базой данных (инкапсуляция)"""
engine = create_engine(SQLALCHEMY_DATABASE_URL)
"""
Строка - создание движка по ней, чтобы скрывать все подробности БД
Сессия - операция
запрашиваю сессию - создается сессия с 2мя параметрами и движком
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
База для декларативной(хочу) базы таблиц: хочу таблицу с такими-то параметрами и колонками
родитель для всех таблиц
"""
Base = declarative_base()

