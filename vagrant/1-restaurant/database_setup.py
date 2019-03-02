import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# ---------CRIAÇÃO DAS TABELAS --------
class Restaurant (Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key = True)
    name = Column(String(250),nullable = False)


class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(250))
    # restaurant_id = Column(Integer,ForeignKey('restaurant.id')
    # restaurant = relationship(Restaurant)
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant) 
    # SERIALIZADO UM ESPACO EM MEMORIA PARA ENVIAR PARA O BANCO
    @property 
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }
# ---------FIM CRIAÇÃO DAS TABELAS --------


engine = create_engine('sqlite:///restaurantmenu.db') # CRIAÇÃO DE UMA ENGINE, ENGINE É UMA BASE PARA A CRIAÇÃO/ CONEXÃO COM O BD

Base.metadata.create_all(engine) # CRIA O BD DE FATO