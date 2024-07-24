import pytest
import urllib.parse


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    client.get('api/parse/', {'input_string': address_string})
    # assert client.get(url)
    # pytest.fail()


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    client.get('api/parse/', {'input_string': address_string})
    # pytest.fail()
