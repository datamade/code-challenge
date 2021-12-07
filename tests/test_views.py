import pytest
from collections import OrderedDict


# Check that API parses valid address
def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'

    response = client.get('/api/parse/?address=' + address_string)

    assert response.status_code == 200
    assert len(response.data) == 3

    assert response.data['input_string'] == '123 main st chicago il'
    assert response.data['address_type'] == 'Street Address'
    assert response.data['address_components'] == OrderedDict([
        ('AddressNumber', '123'),
        ('StreetName', 'main'),
        ('StreetNamePostType', 'st'),
        ('PlaceName', 'chicago'),
        ('StateName', 'il')
    ])


# Check that API raises error with repeated string
def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'

    response = client.get('/api/parse/?address=' + address_string)

    assert response.status_code == 400
    assert response.data['detail'].startswith(
        '\nERROR: Unable to tag this string because more than one area of the string' +
        ' has the same label')
