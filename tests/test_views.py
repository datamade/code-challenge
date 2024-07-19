from urllib.parse import quote


API_URL = '/api/parse/?address='


def test_api_parse_succeeds(client, appropriate_format):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    url_address = quote(address_string)
    response = client.get(f'{API_URL}{url_address}')

    assert response.status_code == 200
    assert response.json() == appropriate_format


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    url_address = quote(address_string)
    response = client.get(f'{API_URL}{url_address}')

    assert response.status_code == 400
    assert "UNCERTAIN LABEL" in str(response.data)
