import pytest
from http import HTTPStatus

API_ENDPOINT = "/api/parse/"


# Although test should have same behavior since it heavily depends on
# the usaaddress library, added tests for different types of address
# to test correct functionality of the API
@pytest.mark.parametrize(
    "address,parsed_components,address_type",
    [
        (
            "123 main st chicago il",
            {
                "AddressNumber": "123",
                "StreetName": "main",
                "StreetNamePostType": "st",
                "PlaceName": "chicago",
                "StateName": "il",
            },
            "Street Address",
        ),  # Example case
        (
            "123 main ave chicago il",
            {
                "AddressNumber": "123",
                "StreetName": "main",
                "StreetNamePostType": "ave",
                "PlaceName": "chicago",
                "StateName": "il",
            },
            "Street Address",
        ),  # Ave instead of St
        (
            "123 main st chicago il 60615",
            {
                "AddressNumber": "123",
                "StreetName": "main",
                "StreetNamePostType": "st",
                "PlaceName": "chicago",
                "StateName": "il",
                "ZipCode": "60615",
            },
            "Street Address",
        ),  # Example case + Zip Code
        # TODO: Add tests for intersection or other address types
    ],
)
def test_api_parse_succeeds(client, address, parsed_components, address_type):

    api_input = {"address": address}

    response = client.get(API_ENDPOINT, api_input)
    address_response_type = response.json()["address_type"]
    address_response_components = response.json()["address_components"]

    assert response.status_code == HTTPStatus.OK
    assert address_response_type == address_type
    assert address_response_components == parsed_components


@pytest.mark.parametrize(
    "address",
    [
        ("123 main st chicago il 123 main st"),  # Repeated street
        ("123 main st chicago il chicago il"),  # Repeated city+state
    ],
)
def test_api_parse_raises_error(client, address):

    api_input = {"address": address}
    response = client.get(API_ENDPOINT, api_input)
    error = response.json()["error"]

    assert error is not None
    assert response.status_code == 400
