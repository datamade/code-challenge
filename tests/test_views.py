import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

def test_api_parse_succeeds(client):
    # Send a request to the API with a valid address
    address_string = '123 main st chicago il'
    response = client.get('/api/parse/', {'address': address_string})

    # Check if the response status code is 200 OK
    assert response.status_code == 200

    # Check if the response contains the expected data
    data = response.json()
    assert 'input_string' in data
    assert data['input_string'] == address_string
    assert 'address_components' in data
    assert 'address_type' in data

    # Check some known components (example, update as needed)
    assert 'AddressNumber' in data['address_components']
    assert data['address_components']['AddressNumber'] == '123'
    assert 'PlaceName' in data['address_components']
    assert data['address_components']['PlaceName'] == 'chicago'
    assert 'StateName' in data['address_components']
    assert data['address_components']['StateName'] == 'il'

def test_api_parse_raises_error(client):
    # Send a request to the API with an invalid address
    address_string = '123 main st chicago il 123 main st'
    response = client.get('/api/parse/', {'address': address_string})

    # Check if the response status code is 400 Bad Request
    assert response.status_code == 400

    # Check if the response contains the error message
    data = response.json()
    assert 'detail' in data
    assert data['detail'] == 'Invalid address' 