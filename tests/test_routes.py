#import pytest
# import app.models.planet import Planet

def test_get_all_planets_with_no_record(client):
    # act:
    response = client.get("/planets")
    response_body = response.get_json()

    # assert:
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet_with_populated_db_returns_planet_json(client, two_saved_planets):
    # act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "Green",
        "radius": 333,
    }


def test_get_one_planet_with_empty_db_returns_404(client):
    # act
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    response_str = "Planet ID 1 not found."
    assert response_body == {"message": response_str}


def test_post_one_planet_creates_planet_in_empty_db(client):
    response = client.post("/planets", json={
        "name": "Jupiter",
        "description": "Jups",
        "radius": 555
    }
    )

    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body
    assert {"id": 1}
