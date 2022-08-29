import json
from django.urls import reverse


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    expected_response = '{"requested_address": "123 main st chicago il",' \
        '"address_parts": {"AddressNumber": "123", "StreetName": "main",' \
        '"StreetNamePostType": "st", "PlaceName": "chicago", "StateName": "il"},'\
        '"address_type": "Street Address"}'

    # Create and call the URL
    url = reverse('address-parse') + "?address=" + address_string
    response = client.get(url)

    # Test the success of the response code
    assert response.json() == json.loads(expected_response)


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    expected_response = "Multiple areas of this address have the same label." \
        " It is likely that either (1) the input string is not a valid address,"\
        " or (2) some tokens were labeled incorrectly."

    # Create and call the URL
    url = reverse('address-parse') + "?address=" + address_string
    response = client.get(url)

    # Test the success of the response code (Should display RepeatedLabelError message)
    assert response.json()["address_parts"] == expected_response
