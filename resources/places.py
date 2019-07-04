from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

places=[{
    'Id':1,
    'name':'Islas del Plastico'},{
    'Id':2,
    'name':'RocaTragon'},{
    'Id':3,
    'name':'Summerfell'},{
    'Id':4,
    'name':'Hot Hill'},{
    'Id':5,
    'name':'Queens Landing'},{
    'Id':6,
    'name':'Days Watch'},{
    'Id':7,
    'name':'Dog Stone'},{
    'Id':8,
    'name':'The Eyes'},{
    'Id':9,
    'name':'Searun'},{
    'Id':10,
    'name':'Castle Rock'}
]

#Micro servicio lugar, con los datos de los distintos lugares
class GoT_Places(Resource):
    def get(self, name):
        for place in places:
            if place['name'].lower() == name.lower(): #Para evitar problemas entre mayusculas y minusculas
                
                return places
        return  'Error 404: El lugar buscado no existe. Consultar con Sadwich Tardy si este personaje existe en los documentos de la Citadel'               
            
    
api.add_resource(GoT_Places, '/v1/places/<string:name>') #http://127.0.0.1./v1/places/...
api.add_resource(GoT_Places, '/v1/places')

app.run(port=8081)
