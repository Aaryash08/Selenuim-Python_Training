import pytest

BASE_URL = "http://127.0.0.1:5000/api"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def patient_data():
    return {
        "name": "Aaryash",
        "age": 22,
        "gender": "Male",
        "disease": "Fever",
        "doctor": "Dr. Sharma"
    }
