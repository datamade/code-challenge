from rest_framework import status
from unittest import TestCase


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = "123 main st chicago il"
    correct_response = {
        "AddressNumber": "123",
        "StreetName": "main",
        "StreetNamePostType": "st",
        "PlaceName": "chicago",
        "StateName": "il"}

    response = client.get("/api/parse/", {"address": address_string})

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["address_type"] == "Street Address"
    TestCase().assertDictEqual(correct_response, response.json()["address_components"])


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = "123 main st chicago il 123 main st"

    response = client.get("/api/parse/", {"address": address_string})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["address_type"] == ""
    assert response.json()["address_components"] == {}
    assert response.json()["error"] == "Cannot parse address with repeated labels"


def test_api_empty_parse_raises_error(client):
    address_string = ""

    response = client.get("/api/parse/", {"address": address_string})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["address_type"] == ""
    assert response.json()["address_components"] == {}
    assert response.json()["error"] == "Address cannot be empty"
