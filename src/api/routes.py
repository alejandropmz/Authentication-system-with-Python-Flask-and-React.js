"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint, jsonify
from api.models import db, User, Favorites, Films, People, Planets, Species, Starships, Vehicles
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

# 4 funciones genericas para el crud : 1 para post, 1 para el get, otra el delete, y put 


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

# ALL USERS

@api.route('/users/', methods=['GET'])
def users():
    users = User.query.filter(User.__tablename__ == "user").all()
    all_users = []

    for i in range(len(users)):
        all_users.append(users[i].serialize())

    if len(all_users) > 0:
        return jsonify({
            "All users":all_users
        })
    
    return jsonify({
        "msg":"No have any user"
    })

# EACH USER

@api.route('/users/<int:user>/', methods=['GET'])
def each_user(user):
    user = User.query.filter(User.id == user).all()
    each_user = user[0].serialize()

    return jsonify({
        "user":each_user
    }), 200

# DELETE USER

@api.route('/users/<int:user>/', methods=['DELETE'])
def delete_user(user):
    users = User.query.filter(User.id == user).first()
    if users is None: # Si no existen usuario entonces imprime el msj que no hay
        return jsonify({
            "msg":"Not have users to delete"
            }), 404

    db.session.delete(users) # Si se salta la condición porque si hay usuarios entonces hace el delete y el commit
    db.session.commit()
    
    return jsonify({
        "msg":"User delete successfully"  # e imprime el msj
    }), 201

# ALL FAVORITES

@api.route('/favorites/', methods=['GET'])
def favorites():
    favorites = Favorites.query.filter(Favorites.__tablename__ == "favorites").all()
    all_favorites = []

    for i in range(len(favorites)):
        all_favorites.append(favorites[i].serialize())
        
    if len(all_favorites) > 0:

        return jsonify({
            "All favorites":all_favorites
        }), 200

    return jsonify({
        "msg":"No have nay favorite"
    })
    



# EACH FAVORITES

@api.route('/favorites/<int:user_param>', methods=['GET'])
def get_user_favorite(user_param): 
    favorites = Favorites.query.filter(Favorites.user_id == user_param).all()
    favorite_list = []
    for_range = len(favorites)

    
    for i in range(for_range):

        if favorites[i].favorite_type == 'films':
            favorites_film = Films.query.get(favorites[i].favorite_id)
            if favorites_film != None:
                favorites[i].serialize()["data"] = favorites_film.serialize()

        if favorites[i].favorite_type == 'people':
            favorites_people = People.query.get(favorites[i].favorite_id)
            if favorites_people != None:
                favorites[i].serialize()["data"] = favorites_people.serialize()
        
        if favorites[i].favorite_type == 'planets':
            favorites_planet = Planets.query.get(favorites[i].favorite_id)
            if favorites_planet != None:
                favorites[i].serialize()["data"] = favorites_planet.serialize()

        if favorites[i].favorite_type == 'species':
            favorites_species = Species.query.get(favorites[i].favorite_id)
            if favorites_species != None:
                favorites[i].serialize()["data"] = favorites_species.serialize()
            
        if favorites[i].favorite_type == 'starships':
            favorites_starships = Starships.query.get(favorites[i].favorite_id)
            if favorites_starships != None:
                favorites[i].serialize()["data"] = favorites_starships.serialize()

        if favorites[i].favorite_type == 'vehicles':
            favorites_vehicles = Vehicles.query.get(favorites[i].favorite_id)
            if favorites_vehicles != None:
                favorites[i].serialize()["data"] = favorites_vehicles.serialize()

        favorite_list.append(favorites[i].serialize())

    return jsonify(favorite_list)


# DELETE FAVORITE

@api.route('/favorites/<int:favorite>/', methods=['DELETE'])
def delete_favorite(favorite):
    favorites = Favorites.query.filter(Favorites.id == favorite).first()
    if favorites is None:
        return jsonify({
            "msg":"Not have favorites to delete"
            }), 404

    db.session.delete(favorites)
    db.session.commit()
    
    return jsonify({
        "msg":"Favorite delete successfully" 
    }), 201


# POST NEW FAVORITE ############################################

@api.route('/favorites/films/<int:film>/', methods=['POST']) # no terminada
def post_favorite(film):
    favorite_type = request.json.get("favorite_type")
    favorite_id = request.json.get("favorite_id")
    post_favorite = Favorites(favorite_type = favorite_type, favorite_id = favorite_id)
    db.session.add(post_favorite)
    db.session.commit()

    return jsonify({
        "msg":"Favorite film create succefully",
        "film":add_film
    }), 200

#/favorite/people/<int:planet_id>


# ALL FILMS

@api.route('/films/', methods=['GET'])
def films():
    films = Films.query.filter(Films.__tablename__ == "films").all()
    all_films = []

    for i in range(len(films)):
        all_films.append(films[i].serialize())

    if len(all_films) > 0:
        
        return jsonify({
            "All films":all_films
        }), 200

    return jsonify({
        "msg":"No have any film"
    })

# EACH FILM

@api.route('/films/<int:film>/', methods=['GET'])
def each_film(film):
    films = Films.query.filter(Films.id == film).first()
    
    if films is None:
        return jsonify({ # Verificar para solventar esta condición
            "film":"Film not found"
        }), 404

    return jsonify({
            "film":films
        }), 201


# DELETE FILM

@api.route('/films/<int:film>/', methods=['DELETE'])
def delete_film(film):
    films = Films.query.filter(Films.id == film).first()

    if films is None:

        return jsonify({
            "msg":"Not have film to delete"
        }), 404

    db.session.delete(films)
    db.session.commit()
    
    return jsonify({
        "msg":"Film delete successfully"
    }), 201

# ALL PEOPLE

@api.route('/people/')
def people():
    people = People.query.filter(People.__tablename__ == "people").all()
    all_people = []

    for i in range(len(people)):
        all_people.append(people[i].serialize())

    if len(all_people) > 0:
        return jsonify({
            "All people":all_people
        }), 200

    return jsonify({
        "msg":"No have any people"
    })


# EACH PEOPLE

@api.route('/people/<int:peop>/', methods=['GET'])
def each_people(peop):
    people = People.query.filter(People.id == peop).first()

    if people is None:
        return jsonify({
            "msg":"people not found"
        }), 404

    return jsonify({
            "people":people
        }), 201


# DELETE PEOPLE

@api.route('/people/<int:peop>/', methods=['DELETE'])
def delete_people(peop):
    people = People.query.filter(People.id == peop).first()

    if people is None:

        return jsonify({
            "msg":"Not have people to delete"
        }), 404
    
    db.session.delete(people)
    db.session.commit()

    return jsonify({
        "msg":"people delete successfully"
    }), 201

# ALL PLANETS

@api.route('/planets/', methods=['GET'])
def planets():
    planets = Planets.query.filter(Planets.__tablename__ == "planets").all()
    all_planets = []

    for i in range(len(planets)):
        all_planets.append(planets[i].serialize())

    if len(all_planets) > 0:
        return jsonify({
            "All planets":all_planets
        }), 200
    return jsonify({
        "msg":"No have any planet"
    })

# EACH PLANET

@api.route('/planets/<int:planet>/')
def each_planet(planet):
    planets = Planets.query.filter(Planets.id == planet).all()
    each_planet = planets[0].serialize()

    if planet <= len(planets)+1: # Verificar para solventar esta condición
        return jsonify({
            "planet":each_planet
        }), 200
    
    return jsonify({
        "msg":"planet not found"
    })

# DELETE PLANET

@api.route('/planets/<int:planet>/', methods=['DELETE'])
def delete_planet(planet):
    planets = Planets.query.filter(Planets.id == planet).first()

    if planets is None:

        return jsonify({
            "msg":"Not have planet to delete"
        }), 404

    db.session.delete(planets)
    db.session.commit()
    
    return jsonify({
        "msg":"planet delete successfully"
    }), 201


# ALL SPECIES

@api.route('/species/')
def species():
    species = Species.query.filter(Species.__tablename__ == "species").all()
    all_species = []

    for i in range(len(species)):
        all_species.append(species[i].serialize())
    
    if len(all_species) > 0:
        return jsonify({
            "All species":all_species
        }), 200
    return jsonify({
        "msg":"no have any specie"
    })


# EACH SPECIE

@api.route('/species/<int:specie>/')
def each_specie(specie):
    species = Species.query.filter(Species.id == specie).all()
    each_specie = species[0].serialize()

    if specie <= len(species)+1: # Verificar para solventar esta condición
        return jsonify({
            "specie":each_specie
        }), 200
    
    return jsonify({
        "msg":"specie not found"
    })

# DELETE SPECIE

@api.route('/species/<int:specie>/', methods=['DELETE'])
def delete_specie(specie):
    species = Species.query.filter(Species.id == specie).first()

    if species is None:

        return jsonify({
            "msg":"Not have specie to delete"
        }), 404
    
    db.session.delete(species)
    db.session.commit()

    return jsonify({
        "msg":"specie delete successfully"
    }), 201

# ALL STARSHIPS

@api.route('/starships/')
def starships():
    starships = Starships.query.filter(Starships.__tablename__ == "starships").all()
    all_starships = []

    for i in range(len(starships)):
        all_starships.append(starships[i].serialize())
    
    if len(all_starships) > 0:
        return jsonify({
            "All starships":all_starships
        }), 200
    return jsonify({
        "msg":"no have any starship"
    })

# EACH STARSHIP

@api.route('/starships/<int:starship>/')
def each_starship(starship):
    starships = Starships.query.filter(Starships.id == starship).all()
    each_starship = starships[0].serialize()

    if starship <= len(starships)+1: # Verificar para solventar esta condición
        return jsonify({
            "starship":each_starship
        }), 200
    
    return jsonify({
        "msg":"starship not found"
    })

# DELETE STARSHIP

@api.route('/starships/<int:starship>/', methods=['DELETE'])
def delte_starship(starship):
    starships = Starships.query.filter(Starships.id == starship).first()

    if starships is None:

        return jsonify({
            "msg":"Not have starship to delete"
        }), 404

    db.session.delete(starships)
    db.session.commit()
    
    return jsonify({
        "msg":"starship delete successfully"
    }), 201


# ALL VEHICLES

@api.route('/vehicles/')
def vehicles():
    vehicles = Vehicles.query.filter(Vehicles.__tablename__ == "vehicles").all()
    all_vehicles = []

    for i in range(len(vehicles)):
        all_vehicles.append(vehicles[i].serialize())
    
    if len(all_vehicles) > 0:
        return jsonify({
            "All vehicles":all_vehicles
        }), 200

    return jsonify({
        "msg":"no have any vehicle"
    })


# EACH VEHICLE

@api.route('/vehicles/<int:vehicle>/')
def each_vehicle(vehicle):
    vehicles = Vehicles.query.filter(Vehicles.id == vehicle).all()
    each_vehicle = vehicles[0].serialize()

    if vehicle <= len(vehicles)+1: # Verificar para solventar esta condición
        return jsonify({
            "vehicle":each_vehicle
        }), 200
    
    return jsonify({
        "msg":"vehicle not found"
    })

# DELETE VEHICLES

@api.route('/vehicles/<int:vehicle>/', methods=['DELETE'])
def delete_vehicle(vehicle):
    vehicles = Vehicles.query.filter(Vehicles.id == vehicle).first()

    if vehicles is None:

        return jsonify({
            "msg":"Not have vehicles to delete"
        }), 404

    db.session.delete(vehicles)
    db.session.commit()
    
    return jsonify({
        "msg":"vehicle delete successfully"
    }), 201

    # 






    """ @api.route('/<string:section>/')
    def all_sections(section):
        element = section
        all_sections = Planets.query.filter(section.capitalize().__tablename__ == section.lower).all()
        elements = []

        for i in range(len(all_sections)):
            elements.append(all_sections[i].serialize())

        if len(elements) > 0:
            return jsonify({
                "data":all_sections
            })
        return jsonify({
            "msg":"data not found"
        }) """


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



