from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_instrutor import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "Fabio's bar")
myFirstItem = MenuItem ( 
    name = 'Frango',
    description = 'Frango grelhado com direito a lagrimas',
    price = 'R$ 15.75',
    restaurant = myFirstRestaurant
    )
session.add(myFirstRestaurant, myFirstItem)
session.commit()
Restaurant_objects = session.query(Restaurant).all()
Menu_items_objetcs = session.query(MenuItem).all()
print(Restaurant_objects)
print(Menu_items_objetcs)