import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_api_parse_succeeds(client):
    # This test verifies that the API successfully parses a valid address
    address_string = '123 main st chicago il'
    response = client.get(reverse('parse_address'), {'address': address_string})
    
    assert response.status_code == 200
    data = response.json()
    assert 'input_string' in data
    assert data['input_string'] == address_string
    assert 'address_components' in data
    assert 'address_type' in data
    assert len(data['address_components']) > 0  # Ensure some components are parsed

@pytest.mark.django_db
def test_api_parse_raises_error(client):
    # This test verifies that the API returns an error for an invalid address
    address_string = '123 main st chicago il 123 main st'
    response = client.get(reverse('parse_address'), {'address': address_string})
    
    assert response.status_code == 400
    data = response.json()
    assert 'error' in data
    assert data['error'] == 'Invalid address format'
