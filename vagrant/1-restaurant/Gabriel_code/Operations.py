from connection import engine 
from banco import Base, User
from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind = engine)
session = DBSession()


def newUser(login,passwd):
    user = User(login = login, password = passwd)
    session.add(user)
    session.commit()
    return True


def readData(Class):
    data = session.query(Class).all()
    for object in data:
        print(object.login) #  THE RETURN IS A LIST
    print()

    first_object = session.query(Class).first()   
    print(first_object.login)
    print()

def updatePassword(login, newPasswd):
    password = session.query(User).filter_by(login = login).first()
    print('Senha antiga : ' + password.password)

    password.password = newPasswd
    session.add(password)
    session.commit()

    password = session.query(User).filter_by(login = login).first()
    print('Senha nova : ' + password.password)
    print()

def deleteUser(login):
    user = session.query(User).filter_by(login = login).first()
    session.delete(user)
    session.commit()
newUser('Ana','BananaPraTu')
readData(User)
# updatePassword('Gabriel','Nova senha')
# deleteUser('Ana')
