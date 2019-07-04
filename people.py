import sqlite3
from db import db

class PeopleModel(db.Model):
    __tablename__='people'

    Id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    isAlive = db.Column(db.Boolean)
    isKing = db.Column(db.Boolean)
    placeId = db.Column(db.Integer)
    
    def __init__(self,name,Id,isAlive,isKing,placeId):
        self.name = name
        self.Id = Id
        self.isAlive = isAlive
        self.isKing = isKing
        self.placeId = placeId

    def json(self):
        return {'name':self.name,'Id':self.Id,'isAlive':self.isAlive,'isKing':self.isKing,'placeId':self.placeId}

    @classmethod
    def find_by_name(cls,name): #Función para encontrar el personaje que queremos leer, crear, cambiar o eliminar
        connection = sqlite3.connect('people.db')
        cursor = connection.cursor()

        query = "SELECT * FROM people WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row) #pasar todas las posiciones de row

    def insert(self):
        connection = sqlite3.connect('people.db')
        cursor=connection.cursor()

        query = "INSERT INTO people VALUES (?,?,?,?,?)"
        cursor.execute(query, (self.name,self.Id,self.isAlive,self.isKing,self.placeId))
        connection.commit()
        connection.close()

    def update(self):
        connection=sqlite3.connect('people.db')
        cursor = connection.cursor()

        queryID = "UPDATE people SET Id=? WHERE name=?"
        queryAlive = "UPDATE people SET isAlive=? WHERE name=?"
        queryKing = "UPDATE people SET isKing=? WHERE name=?"
        queryPlace = "UPDATE people SET placeId=? WHERE name=?"

        cursor.execute(queryID, (self.name,self.Id))
        cursor.execute(queryAlive, (self.name,self.isAlive))
        cursor.execute(queryKing, (self.name,self.isKing))
        cursor.execute(queryPlace, (self.name,self.placeId))
        
        connection.commit()
        connection.close()
        
