import pytest

from parserator_web.views import AddressParse
from rest_framework.exceptions import ParseError


def test_parse_method():
    address_string = "123 main st chicago il"
    self = AddressParse

    return_obj = AddressParse.parse(self, address_string)

    assert return_obj[0] == {
      'AddressNumber': '123',
      'StreetName': 'main',
      'StreetNamePostType': 'st',
      'PlaceName': 'chicago',
      'StateName': 'il'
    }
    assert return_obj[1] == 'Street Address'


def test_parse_method_invalid_address():
    address_string = '123 main st chicago il 123 main st'
    self = AddressParse

    with pytest.raises(ParseError):
        AddressParse.parse(self, address_string)
