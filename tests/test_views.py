import pytest


def test_api_parse_succeeds(client):

    address_string = '123 main st chicago il'
    url = f'/api/parse/?address={address_string}'

    response = client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data['input_string'] == address_string
    assert 'address_components' in data
    assert 'address_type' in data

    assert isinstance(data['input_string'], str)
    assert isinstance(data['address_components'], dict)
    assert isinstance(data['address_type'], str)


def test_api_parse_raises_error(client):

    address_string = '123 main st chicago il 123 main st'
    url = f'/api/parse/?address={address_string}'

    response = client.get(url)
    assert response.status_code == 400
