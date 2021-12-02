from typing import OrderedDict
import pytest


def test_api_parse_succeeds(client, url):
    address_string = '123 main st chicago il'

    # Call the API with the address to be tested
    response = client.get(url, {'address': address_string})

    # Confirm the data comes back in the appropriate format
    assert response.data['input_string'] == address_string
    assert response.data['address_components'] == \
        OrderedDict([('AddressNumber', '123'),
                    ('StreetName', 'main'),
                    ('StreetNamePostType', 'st'),
                    ('PlaceName', 'chicago'),
                    ('StateName', 'il')])
    assert response.data['address_type'] == 'Street Address'


def test_api_parse_raises_error(client, url):
    address_string = '123 main st chicago il 123 main st'

    # Call the API with the address to be tested
    response = client.get(url, {'address': address_string})

    # Confirm the data comes back in the appropriate format
    assert response.data['input_string'] == address_string
    assert response.data['address_components'] == ''
    assert response.data['address_type'] == 'Invalid'
    assert response.status_code == 400
