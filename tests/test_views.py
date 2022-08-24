from django.urls import reverse


def get_response(client, address_string):
    url = reverse("address-parse")
    url += "?address=" + "+".join(address_string.split())
    return client.get(url)


def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    response = get_response(client, address_string)
    assert response.data == {"input_string": "123 main st chicago il",
                             "address_components": {"AddressNumber": "123",
                                                    "StreetName": "main",
                                                    "StreetNamePostType": "st",
                                                    "PlaceName": "chicago",
                                                    "StateName": "il"},
                             "address_type": "Street Address"}


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    response = get_response(client, address_string)
    assert response.data == {"address_type": "Error: "
                                             "err=RepeatedLabelError('"
                                             "123 main st chicago il 123 main st', "
                                             "[('123', 'AddressNumber'), "
                                             "('main', 'StreetName'), "
                                             "('st', 'StreetNamePostType'), "
                                             "('chicago', 'PlaceName'), "
                                             "('il', 'StateName'), "
                                             "('123', 'AddressNumber'), "
                                             "('main', 'StreetName'), "
                                             "('st', 'StreetNamePostType')],"
                                             " 'AddressNumber')"}
