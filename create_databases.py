#
#Este archivo .py genera dos tablas: UNa de personajes y otra de lugares.
#Debe ser corrido antes de correr el server "app.py"
#
#La base de datos de las personas es "people.db", dara servicio al microservicio de los personajes
#-Un personaje tiene Id, Nombre, si es rey o no (boolean), si esta vivo o no (boolean) y el Id del lugar
#
#La base de datos de los lugares es "places.db", dara servicio al microservicio de los lugares
#-Un lugar tiene Id y nombre

import sqlite3

#Creando la conexion a la base de datos de los personajes
connection = sqlite3.connect('people.db')
cursor = connection.cursor() #Responsable de las solicitudes y guardar los resultados
#Creando la tabla de los personajes
create_people = "CREATE TABLE IF NOT EXISTS people (Id int, name text, isAlive bool, isKing bool, placeId int)"
cursor.execute(create_people)

#Creamos algunos personajes
people=[
    (1, "Tirio Greytoy", True, True, 4),
    (2, "Jaime Salchister", True, False, 1),
    (3, "Sandwich Tarly", True, False, 5),
    (4, "Selena Salchister", True, True, 2),
    (5, "Sara Shark", True, False, 3),
    (6, "John Rain", True, True, 8),
    (7, "Daniela Targetian", True, True, 2),
    (8, "Bigfinger", True, False, 8),
    (9, "Catalina Tuty", True, False, 2),
    (10, "Tintin Salchister", True, False, 3)
]

insert_query = "INSERT INTO people VALUES (?, ?, ?, ?, ?)"
cursor.executemany(insert_query, people)
connection.commit()
#Cerramos la conexion
connection.close()

#Conexion para los lugares
connection = sqlite3.connect('places.db')
cursor = connection.cursor()

create_places = "CREATE TABLE IF NOT EXISTS places (Id int, name text)"
cursor.execute(create_places)

#Creamos algunos lugares
places=[
    (1,"Queens Landing"),
    (2,"Hot Hill"),
    (3,"The Eyes"),
    (4,"Summerfell"),
    (5,"Islas del Plastico"),
    (6,"RocaTragon"),
    (7,"Days Watch"),
    (8,"Dog Stone"),
    (9,"Searun"),
    (10,"Castle Rock")
]

insert_query = "INSERT INTO places VALUES (?, ?)"
cursor.executemany(insert_query, places)
connection.commit()
connection.close()


