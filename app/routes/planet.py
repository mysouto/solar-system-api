from crypt import methods
import json
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")


def make_planet_dict(planet):
    planet_dict = {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "radius": planet.radius
    }

    return planet_dict


# validate planet
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response_str = f"Planet ID {planet_id} invalid. ID must be an integer."
        abort(make_response({"message": response_str}, 400))

    planet = Planet.query.get(planet_id)

    # 404 not found
    if not planet:
        response_str = f"Planet ID {planet_id} not found."
        abort(make_response({"message": response_str}, 404))

    return planet


@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    response = []
    for planet in planets:
        planet_dict = make_planet_dict(planet)

        response.append(planet_dict)

    return jsonify(response), 200


@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    # planet = Planet.query.get(planet_id)
    planet = validate_planet(planet_id)

    planet_dict = make_planet_dict(planet)

    return jsonify(planet_dict), 200


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


@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet_id} successfully deleted.")


@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

# put if clause in helper function?
    if "name" not in request_body or \
        "description" not in request_body or \
            "radius" not in request_body:
        return jsonify({"message": "Request must include name, description, and radius"}), 400

    planet.name = request_body['name']
    planet.description = request_body['description']
    planet.radius = request_body['radius']

    db.session.commit()

    return make_response(f"Planet {planet_id} updated successfully", 200)


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
