from connect import conexao
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
base = declarative_base()

class Restaurant(base):
	__tablename__ = 'restaurant'
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)

class MenuItem(base):
	__tablename__ = 'menu_item'
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	desc = Column(String(250))
	price = Column(String(250))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)
	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'desc': self.desc,
			'price': self.price
		}

base.metadata.create_all(conexao)


