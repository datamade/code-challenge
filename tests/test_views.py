import pytest
from django.urls import reverse
from rest_framework.test import APIClient


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    response = client.get(reverse('address-parse'), {'address': address_string})

    assert response.status_code == 200

    json_data = response.json()

    assert "input_string" in json_data
    assert "address_components" in json_data
    assert "address_type" in json_data

    pytest.fail()


def test_api_parse_raises_error(client):
    # Send a request to the API with an address string that will raise a RepeatedLabelError
    address_string = '123 main st chicago il 123 main st'
    response = client.get(reverse('address-parse'), {'address': address_string})
    
    # Check that the response status code is 400 Bad Request
    assert response.status_code == 400
    
    # Check that the response contains the 'error' key
    json_data = response.json()
    assert 'error' in json_data
    pytest.fail()
