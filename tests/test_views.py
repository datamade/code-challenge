import pytest


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    address_string_url = "+".join(address_string.split())
    assert client.get(f"/api/parse/?address={address_string_url}").status_code == 200


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    address_string_url = "+".join(address_string.split())
    assert client.get(f"/api/parse/?address={address_string_url}").status_code == 400
