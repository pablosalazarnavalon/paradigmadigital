import sqlite3
import os
import sys
from flask_restful import Resource, reqparse
maindir=os.path.dirname(os.path.abspath(__file__))+"/../"
sys.path.append(maindir)
from models.people import PeopleModel
#Main application for the wiki of Game of Thrones

class People(Resource):   
    def get(self):
        connection = sqlite3.connect('people.db')
        cursor = connection.cursor()

        query = "SELECT * FROM people"
        result = cursor.execute(query)
        people= []
        for row in result:
            people.append({'Id':row[0],'name':row[1],'isAlive':row[2],'isKing':row[3],'placeId':row[4]})
            
        connection.close()
        return {'people':people}

class Character(Resource):
    #Argumentos que deben ser especificados en caso de creación o actualización de un personaje (isAlive, king, y placeId), el Id es dado el siguiente no utilizado en la lista de personajes
    parser = reqparse.RequestParser()
    parser.add_argument('Id', type=int,required=True, help="El Id del personaje debe ser especificado")
    parser.add_argument('isAlive', type=bool, default=False,required=False, help="Si el usuario no especifica si el personaje esta vivo o muerto, se le da por muerto")
    parser.add_argument('isKing', type=bool, default=False, required=False, help="Debe ser especificado si el personaje es rey o no")
    parser.add_argument('placeId', type=int, required=False, help="El lugar del personaje debe ser especificado")

    def get(self, name):
        character = PeopleModel.find_by_name(name)
        if character:
            return character.json()
        return {'message':'El personaje buscado no existe, consultar con Sandwich Tardy si hay registros suyos en la Citadel'}
        
    def post(self, name):
        #Si el usuario intenta crear un personaje ya existente en la base de datos, la solicitud del usuario es incorrecta. Hay que avisar al usuario, y devolver el codigo 400 (bad-request)
        if PeopleModel.find_by_name(name):
            return {'message': 'El personaje '+str(name)+' ya existe.'}, 400 

        data = Character.parser.parse_args()
        character = PeopleModel(name,data['Id'],data['isAlive'],data['isKing'],data['placeId'])
        try:
           character.insert()
           return character.json()
        except:
            return {'message':'Error al intentar añadir el personaje a la base de datos'}, 500 #Http: Devolvemos un internal-server-error

    def delete(self,name):
        #Para borrar, necesitamos una lista, esta lista son todos los personajes, menos el que buscamos borrar
        if PeopleModel.find_by_name(name):
            connection = sqlite3.connect('people.db')
            cursor = connection.cursor()
            query = "DELETE FROM people WHERE name=?"
            cursor.execute(query,(name,))
            connection.commit()
            connection.close()
        
            return {'message':str(name)+' fue eliminado.'}
        else:
            return {'message':str(name)+' no existe. ¿Está ya muerto?'}

    def put(self,name):
        data = Character.parser.parse_args()

        character = PeopleModel.find_by_name(name)
        updated_character = PeopleModel(name,data['Id'],data['isAlive'],data['placeId'],data['isKing'])
        
        if character is None:
            try:
                updated_character.insert()
            except:
                return {"message":"Error al añadir el personaje"}, 500
        else:
            try:
                updated_character.update()
            except:
                return {"message":"Error al actualizar el personaje"}, 500
        return character #Return el character actualizado/creado para reflejar el cambio

        
    

