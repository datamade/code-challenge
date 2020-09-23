import pytest

def test_api_parse_succeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    res = client.get("/api/parse", {"address": address_string})
    assert res.status_code == 200


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    res = client.get("/api/parse", {"address": address_string})
    assert res.status_code == 500

## These tests don't work, I don't have a lot of experience with Django and I ran out of time, sorry!
