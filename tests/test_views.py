import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_api_parse_succeeds(client):
    """
    Test Behavior: verifies the API successfully parses a valid string address
    With a valid address string the API returns:
    input_string-- original address string from user
    address_components-- dictionary of parsed components
    address_type-- string representing the type of parsed address
    """
    address_string = '123 main st chicago il'

    # create instance of test client
    client = APIClient()

    # send get request to API endpoint with address string
    response = client.get('/api/address-parse/', {'address': address_string})

    # ensure response status code is 200
    assert response.status_code == 200

    # check response contains expected keys
    expected_keys = {'input_string', 'address_components', 'address_type'}
    assert set(response.data.keys()) == expected_keys

    # ensure input string matches address string
    assert response.data['input_string'] == address_string

    # check address_components and address_type aren't empty
    assert response.data['address_components']
    assert response.data['address_type']
    # removed pytest.fail()


@pytest.mark.django_db
def test_api_parse_raises_error(client):
    """
    Test Behavior: verify the API correctly handles the invalid address strings that
    cause RepeatedLabelError. With an invalid string address the API returns an error
    message with status code of 400.
    """
    # invalid address string causes RepeatedLabelError,
    # so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'

    # create instance for test client
    client = APIClient()

    # send get request to API endpoint with invalid address string
    response = client.get('/api/address-parse/', {'address': address_string})

    # ensure response status code is 400
    assert response.status_code == 400

    # check response contains error keys
    assert 'error' in response.data

    # check error message is not empty
    assert response.data['error']

    # removed pytest.fail()
