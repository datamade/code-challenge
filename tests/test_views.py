def test_api_parse_succeeds(client):
    input_string = "123 main st chicago il"

    response = client.get('/api/parse/', {'input_string': input_string})

    assert response.status_code == 200
    assert response.data["input_string"] == input_string
    assert response.data["address_type"] == "Street Address"
    assert response.data['address_components'] == {
        'AddressNumber': '123',
        'StreetName': 'main',
        'StreetNamePostType': 'st',
        'PlaceName': 'chicago',
        'StateName': 'il'
    }


def test_api_parse_raises_error(client):
    invalid_input_string = '123 main st chicago il 123 main st'

    response = client.get('/api/parse/', {'input_string': invalid_input_string})

    assert response.status_code == 400
