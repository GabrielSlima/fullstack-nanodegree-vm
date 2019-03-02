from connect import conexao
from sqlalchemy.orm import sessionmaker
from banco import Restaurant, MenuItem

DBSession = sessionmaker(bind = conexao)
session = DBSession()


def insertRestaurant(restaurant_name):
	restaurant = Restaurant(name = restaurant_name)
	session.add(restaurant)
	session.commit()
	return True
def readAllRestaurantData():
	data = session.query(Restaurant)
	all_data = {}
	for i in data:
		all_data.setdefault(i.id,i.name)
		print(i.id, end=', ')
		print(i.name)
	print(all_data)
	return all_data
def getAllRestaurantNames():
	data = session.query(Restaurant)
	all_data = []
	for i in data:
		all_data += [i.name]
	return all_data

def editRestaurant(restaurantId, newName):
	try:
		restaurant = session.query(Restaurant).filter_by(id = restaurantId).first()
		restaurant.name = newName
		session.add(restaurant)
		session.commit()
		return True
	except AttributeError:
		return False

def deleteRestaurant(restaurantId):
	try:
		restaurant = session.query(Restaurant).filter_by(id= restaurantId).first()
		session.delete(restaurant)
		session.commit()
		return True
	except AttributeError:
		return False
if __name__ == '__main__':
	#all_dadush = readAllRestaurantData()
	insertRestaurant('Davi esta viciado em Fortnite')
	dadush = getAllRestaurantNames()
	print(dadush)
	#print(all_dadush)
	#print (editRestaurant(33,'Martinho lutero - Feijoada'))
	#print(deleteRestaurant(1))
