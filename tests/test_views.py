REQUEST_URL = "/api/parse/"

def test_api_parse_succeeds(client):
    # should also be the 'input_string' in the response
    address_string = '123 main st chicago il'
    request_data = { "address": address_string }
    # make GET request, store response in 'response' variable
    response = client.get(REQUEST_URL, request_data)

    # What the 'address_components' part of response.data should look like
    # Using dictionaries will simplify looking up and comparing keys/values
    valid_components_dict = {
        "AddressNumber": "123",
        "StreetName": "main",
        "StreetNamePostType": "st",
        "PlaceName": "chicago",
        "StateName": "il",
    }
    # What 'address_components' components actually looks like 
    response_components_dict = dict(response.data["address_components"])

    # Confirm each key/value in the expected response's address_components matches every key/value in the actual response
    for key in valid_components_dict:
        assert valid_components_dict[key] == response_components_dict[key]

    # Confirm the other 2 fields are also as expected
    assert response.data["input_string"] == address_string
    assert response.data["address_type"] == "Street Address"

# def test_api_parse_raises_error(client):
#     # TODO: Finish this test. The address_string below will raise a
#     # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
#     address_string = '123 main st chicago il 123 main st'
#     pytest.fail()
