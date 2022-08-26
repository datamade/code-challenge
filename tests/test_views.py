def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    response = client.get(f"/api/parse/?address={address_string}")
    expected_response = {
        'input_string': address_string,
        'address_components': 
        {'AddressNumber': '123',
        'StreetName': 'main',
        'StreetNamePostType': 'st',
        'PlaceName': 'chicago',
        'StateName': 'il'
        },
        'address_type': 'Street Address'  
    }

    assert expected_response == response.json()


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    response = client.get(f"/api/parse/?address={address_string}")
    assert response.json()["error"] == "Sorry, we couldn't parse this address. Please check your address and try again!"
