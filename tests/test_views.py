from ast import Add
import pytest
from parserator_web.views import AddressParse
from django.urls import reverse


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    url = reverse('address-parse') + f'?input={address_string}'
    response = client.get(url).json()
    assert response['input_string'] == address_string 
    assert response['address_components']['AddressNumber'] == '123'
    assert response['address_components']['StreetName'] == 'main'
    assert response['address_components']['StreetNamePostType'] == 'st'
    assert response['address_components']['StateName'] == 'il'
    assert response['address_type'] == 'Street Address'

def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    url = reverse('address-parse') + f'?input={address_string}'
    response = client.get(url).json()
    assert response['error']
