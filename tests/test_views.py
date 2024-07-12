import json

parse_url = "/api/parse/"


def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    response = client.get(parse_url, {"address": address_string})

    assert response.status_code == 200

    parsed_data = json.loads(response.content)
    assert parsed_data == {
        "input_string": "123 main st chicago il",
        "address_components": {
            "AddressNumber": "123",
            "StreetName": "main",
            "StreetNamePostType": "st",
            "PlaceName": "chicago",
            "StateName": "il"
        },
        "address_type": "Street Address"
    }


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    response = client.get(parse_url, {"address": address_string})

    assert response.status_code == 400


def test_api_parse_raises_error_on_missing_address_string(client):
    response = client.get(parse_url, {})

    assert response.status_code == 400


def test_api_parse_succeeds_on_empty_string(client):
    address_string = ""
    response = client.get(parse_url, {"address": address_string})

    assert response.status_code == 200
