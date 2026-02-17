import pytest

BASE_URL = "http://127.0.0.1:5000/api"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def sample_movie():
    return {
        "id": 1,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m"
    }
