import pytest
from django.test import Client

def test_api_parse_succeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    c = Client()
    response = c.get('/api/parse/', {'address': address_string})
    assert response.status_code == 200
    # pytest.fail()


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    c = Client()
    response = c.get('/api/parse/', {'address': address_string})
    assert response.status_code == 400
    # pytest.fail()
