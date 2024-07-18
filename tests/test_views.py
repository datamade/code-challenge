""""""

from http import HTTPStatus

PARSE_API = "/api/parse/"


def test_api_parse_succeeds(client):
    """
    Tests the API by sending an address
    """
    address_string = "123 main st chicago il"
    correct_answer = {
        "AddressNumber": "123",
        "StreetName": "main",
        "StreetNamePostType": "st",
        "PlaceName": "chicago",
        "StateName": "il",
    }

    correct_address_type = "Street Address"

    payload = {"address": address_string}

    # Invoking API and getting response contents
    response = client.get(PARSE_API, payload)
    address_type = response.json()["address_type"]
    components = response.json()["address_components"]

    assert response.status_code == HTTPStatus.OK
    assert address_type == correct_address_type
    assert components == correct_answer


def test_api_parse_raises_error(client):
    """
    Verify API raises an error
    """

    address_string = "123 main st chicago il 123 main st"

    payload = {"address": address_string}

    # Invoking API and getting response contents
    response = client.get(PARSE_API, payload)
    address_type = response.json()["address_type"]
    error = response.json()["error"]

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert address_type == ""
    assert error is not None
