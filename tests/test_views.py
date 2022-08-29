import pytest
from parserator_web.views import AddressParse


def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    result = AddressParse.parse(client,address=address_string)

    #if the result is not as expected, fail this test and return the actual result.
    if result !=  ([('123', 'AddressNumber'), ('main', 'StreetName'), ('st', 'StreetNamePostType'), ('chicago', 'PlaceName'), ('il', 'StateName')], 'Street Address'):
        pytest.fail("Incorrect format. Instead got {0}".format(result))


def test_api_parse_raises_error(client):
    #Try to parse the address string, break if there is an exeception (which should happen). If there isn't an exeception, fail this test.
    address_string = '123 main st chicago il 123 main st'
    try:
        AddressParse.parse(client, address=address_string)
    except Exception as e:
        return
    pytest.fail("Missed exeception!")
