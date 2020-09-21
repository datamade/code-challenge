import pytest
from urllib.parse import urlencode
import usaddress


def test_api_parse_succeds(client):
    address_string = '123 main st chicago il'
    test_address_components, test_address_type = usaddress.tag(address_string)
    get_param = urlencode({'address': address_string}) 

    response = client.get(f'/api/parse/?{get_param}')
    assert response.status_code == 200
    assert response.data['input_string'] == '123 main st chicago il' 
    assert response.data['address_components'] == test_address_components
    assert response.data['address_type'] == test_address_type

def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    get_param = urlencode({'address': address_string}) 
    response = client.get(f'/api/parse/?{get_param}')
    assert response.status_code == 400
    assert response.data['detail'] == "Unable to parse this value due to repeated labels. Please correct and resubmit"
