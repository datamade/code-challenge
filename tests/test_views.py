import pytest


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    response = client.get("/api/parse", {"address": address_string}, follow=True)
    expected_answer = {"payload": [
        {
            "AddressNumber": "123",
            "StreetName": "main",
            "StreetNamePostType": "st",
            "PlaceName": "chicago",
            "StateName": "il"
        },
        "Street Address"
        ],
     "errors": ""
     }
    if response.json()['errors'] != '':
        pytest.fail()
    assert response.json()['payload'] == expected_answer['payload']


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    response = client.get("/api/parse", {"address": address_string}, follow=True)
    expected_answer = {
        "payload": "",
        "errors": "Repeated Labels"
        }
    if response.json()['errors'] == '':
        pytest.fail()
    assert response.json()['errors'] == expected_answer['errors']
