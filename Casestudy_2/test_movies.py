import requests
import pytest

def test_fetch_all_movies(base_url):
    response = requests.get(f"{base_url}/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_new_movie(base_url, sample_movie):
    response = requests.post(f"{base_url}/movies", json=sample_movie)
    assert response.status_code == 201
    assert response.json()["movie_name"] == "Interstellar"


def test_get_movie_by_id(base_url):
    response = requests.get(f"{base_url}/movies/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_movie(base_url):
    payload = {"movie_name": "Interstellar Updated"}
    response = requests.put(f"{base_url}/movies/1", json=payload)
    assert response.status_code == 200
    assert response.json()["movie_name"] == "Interstellar Updated"


def test_delete_movie(base_url):
    response = requests.delete(f"{base_url}/movies/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Movie deleted"


@pytest.mark.parametrize("payload, expected_status", [
    ({"movie_id": 1, "seats": 2}, 201),
    ({}, 400),
    ({"movie_id": 1}, 400),
])
def test_book_ticket(base_url, payload, expected_status):
    response = requests.post(f"{base_url}/bookings", json=payload)
    assert response.status_code == expected_status
