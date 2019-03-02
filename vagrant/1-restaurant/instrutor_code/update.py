from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_instrutor import Base, Restaurant, MenuItem
from create import DBSession, session

Restaurant_objects = session.query(Restaurant).all()
Menu_items_objetcs = session.query(MenuItem).all()
firstItem = session.query(Restaurant).first()

for item in Restaurant_objects:
    print(item.id)