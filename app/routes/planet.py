import json
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    response = []
    for planet in planets:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "radius": planet.radius
        }

        response.append(planet_dict)

    return jsonify(response), 200


@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        radius=request_body["radius"],
    )

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201


# @planet_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     planet_dict = {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description
#     }

#     return jsonify(planet_dict), 200

    # bonus: create planet dict helper function


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         response_str = f"Invalid planet id: {planet_id}. ID must be an integer."
#         abort(make_response({"message": response_str}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     response_str = f"Could not find planet: {planet_id}."
#     abort(make_response({"message": response_str}, 404))

# planets = [
#     Planet(1, "Mercury", "gray"),
#     Planet(2, "Venus", "orange"),
#     Planet(3, "Earth", "green for now"),
#     Planet(4, "Mars", "red and hot"),
#     Planet(5, "Jupiter", "gassy"),
#     Planet(6, "Saturn", "has rings"),
#     Planet(7, "Uranus", "light grey"),
#     Planet(8, "Neptune", "cute blue")
# ]
