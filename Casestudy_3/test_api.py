import requests
import pytest

def test_add_patient(base_url, patient_data):
    response = requests.post(f"{base_url}/patients", json=patient_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Aaryash"

def test_get_patients(base_url):
    response = requests.get(f"{base_url}/patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.parametrize("payload", [
    {},
    {"name": "Test"},
])
def test_invalid_patient(base_url, payload):
    response = requests.post(f"{base_url}/patients", json=payload)
    assert response.status_code == 400

@pytest.mark.skip(reason="Feature under development")
def test_skip_example():
    assert False

@pytest.mark.xfail
def test_expected_failure():
    assert 1 == 2
