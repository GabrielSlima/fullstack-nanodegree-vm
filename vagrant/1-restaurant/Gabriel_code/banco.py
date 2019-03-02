from connection import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    login = Column(String(30), nullable = False)
    password = Column(String(30), nullable = False)

Base.metadata.create_all(engine)
Base.metadata.bind = engine
