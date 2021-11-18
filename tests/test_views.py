def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    response = client.get('/api/parse/', {'address': address_string})
    assert response.status_code == 200


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    response = client.get('/api/parse/', {'address': address_string})
    assert response.status_code == 400