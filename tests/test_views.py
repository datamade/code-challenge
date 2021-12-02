from typing import OrderedDict
import pytest
from django.urls import reverse

def test_api_parse_succeeds(client,url):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'

    # Call the API with the address to be tested
    response = client.get(url, {'address': address_string})
    
    # Confirm the data comes back in the appropriate format
    # assert response.data == address_string
    assert response.data['input_string'] == address_string
    assert response.data['address_components'] == OrderedDict([('AddressNumber', '123'), ('StreetName', 'main'), ('StreetNamePostType', 'st'), ('PlaceName', 'chicago'), ('StateName', 'il')])
    assert response.data['address_type'] == 'Street Address'


def test_api_parse_raises_error(client,url):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'

    # Call the API with the address to be tested
    response = client.get(url, {'address': address_string})

    assert response.data['input_string'] == address_string
    assert response.data['address_components'] == ''
    assert response.data['address_type'] == 'Invalid'
    assert response.status_code == 400
