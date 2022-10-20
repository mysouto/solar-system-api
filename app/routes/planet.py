import json
from pydoc import describe
from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


planets = [
    Planet(1, "Mercury", "gray"),
    Planet(2, "Venus", "orange"),
    Planet(3, "Earth", "green for now"),
    Planet(4, "Mars", "red and hot"),
    Planet(5, "Jupiter", "gassy"),
    Planet(6, "Saturn", "has rings"),
    Planet(7, "Uranus", "light grey"),
    Planet(8, "Neptune", "cute blue")
]

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET"])
def get_all_planets():
    response = []
    for planet in planets:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        }

        response.append(planet_dict)

    return jsonify(response), 200
