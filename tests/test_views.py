import pytest
import json
from django.urls import reverse

def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    address_list = address_string.split(" ")
    url=reverse('address-parse')
    response = client.get(url, {'address': address_string})
    parsedResponse = json.loads(response.content.decode('utf8'))
    assert response.status_code == 200
    assert parsedResponse['input_string'] == address_string
    assert parsedResponse['address_type'] == 'Street Address'
    for piece in address_list:
        assert piece in parsedResponse['address_components'].values()


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    url=reverse('address-parse')
    response = client.get(url, {'address': address_string})
    assert response.status_code == 400
    #pytest.fail()
