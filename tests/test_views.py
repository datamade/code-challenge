import json
import usaddress
from django.urls import reverse


def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    url = reverse('address-parse')
    response = client.get(url, {'address': address_string})
    parsedResponse = json.loads(response.content.decode('utf8'))
    apiParse = usaddress.tag(address_string)
    assert response.status_code == 200
    assert parsedResponse['input_string'] == address_string
    assert parsedResponse['address_type'] == apiParse[1]
    assert parsedResponse['address_components'] == apiParse[0]


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    url = reverse('address-parse')
    response = client.get(url, {'address': address_string})
    assert response.status_code == 400
