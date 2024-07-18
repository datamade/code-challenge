def test_api_parse_succeeds(client):
    # We're going to test just the status code and json of the response
    # Testing of e.g., templates or contexts should be done elsewhere
    address_string = '123 main st chicago il'
    response = client.get("/api/parse", {"address": address_string}, follow=True)
    assert response.json() == {"address_components": [["AddressNumber", "123"],
                                                      ["StreetName", "main"],
                                                      ["StreetNamePostType", "st"],
                                                      ["PlaceName", "chicago"],
                                                      ["StateName", "il"]],
                               "address_type": "Street Address",
                               "input_string": "123 main st chicago il"}
    assert response.status_code == 200


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    response = client.get("/api/parse", {"address": address_string}, follow=True)
    assert response.json() == {"error": "This address failed to parse"}
    assert response.status_code == 400
