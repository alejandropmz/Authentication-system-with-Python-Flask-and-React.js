"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint, jsonify
from api.models import db, User, Favorites, Films, Planets
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

""" @api.route('/todos/<int:user_param>', methods=['GET'])
def get_todos(user_param):
    todos=Todos.query.filter(Todos.user_id==user_param).all() #Se especifica entonces que traemos todos los todos y el user_param va a ser el mismo valor que el user_id del todo
    user_data = todos[0].user.serialize() # se trae el primer parametro de la colección que se crea en la línea de codigo de arriba
    return jsonify({ #aquí se retorna toda la información de los todos junto a la del usuario
        "user":user_data,
        "todos":list(map(lambda item:item.serialize(),todos))
    }), 200

    
@api.route('/todos/<int:user_param>', methods=['POST']) #aqui le damos la distinción a cada ruta para que los todos sean independientes para cada usuario
def post_todo(user_param):
    label = request.json.get("label") #aqui se define que información es la cual se va a cargar cuando se haga el post en la aplicación
    done = request.json.get("done") #aqui se define que información es la cual se va a cargar cuando se haga el post en la aplicación
    newTodo = Todos(user_id=user_param, label=label, done=done) #aquí se crea el newtodo
    db.session.add(newTodo) #aquí se agrega a la base de datos
    db.session.commit() #aquí se envia la actualización
    return jsonify({"reply":"Todo created successfully"}), 201 #La respuesta que se muestra al momento de hacer el post, en este caso en el postman

@api.route('/todos/<int:user_param>/<int:todo_index>', methods=['PUT'])
def put_todo(user_param, todo_index):
    label = request.json.get("label")
    done = request.json.get("done")
    todos = Todos.query.filter(Todos.user_id==user_param).all()
    newTodo = todos[todo_index]
    newTodo.label = label
    newTodo.done = done
    db.session.add(newTodo)
    db.session.commit()
    return jsonify({"reply":"Todo update successfully"}), 200


@api.route('/todos/<int:user_param>/<int:todo_index>', methods=['DELETE'])
def delete_todo(user_param, todo_index):
    todos=Todos.query.filter(Todos.user_id==user_param).all()
    deleteTodo = todos[todo_index]
    db.session.delete(deleteTodo)
    db.session.commit()
    return jsonify({"reply":"Todo delete successfully"}), 200 """


@api.route('/favorites/<int:user_param>', methods=['GET'])
def get_favorites(user_param):
    favorites = Favorites.query.filter(Favorites.user_id == user_param).all()
    favorite_list = []
    for_range = len(favorites)

    
    for i in range(for_range):
        
        if favorites[i].favorite_type == 'planets':
            favorites_planet = Planets.query.get(favorites[i].favorite_id)
            favorites[i].serialize()["data"] = favorites_planet.serialize()

    return jsonify(favorite_list)
    
    #list(map(lambda favorite: favorite.serialize(), favorites)), 200





