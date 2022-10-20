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
