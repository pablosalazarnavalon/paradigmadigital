import sqlite3
from flask import Flask, request
from flask_restful import Api
from resources.people import People, Character

app = Flask(__name__)
api = Api(app)

api.add_resource(People, '/v1/people') #http://127.0.0.1.8082/v1/people, this URL prints all people
api.add_resource(Character, '/v1/people/<string:name>') #http://127.0.0.1.8082/v1/people/<name>, this URL prints a single character


if __name__ == '__main__':
    app.run(port=8082,debug=True)
