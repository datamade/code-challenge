import pytest
from django.urls import reverse
from rest_framework import status


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    url = reverse('address-parse')
    response = client.get(url, {'address': address_string})
    
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert 'input_string' in data
    assert 'address_components' in data
    assert 'address_type' in data
    
    assert data['input_string'] == address_string
    assert 'AddressNumber' in data['address_components']
    assert data['address_components']['AddressNumber'] == '123'
    assert data['address_type'] == 'Street Address'


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    url = reverse('address-parse')
    response = client.get(url, {'address': address_string})
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'Error parsing address' in response.json()['detail']


# Additional test for missing address parameter
def test_api_parse_missing_address(client):
    url = reverse('address-parse')
    response = client.get(url)
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'Address parameter is required' in response.json()['detail']