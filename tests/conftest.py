# Define test fixtures here.
import pytest


@pytest.fixture
def appropriate_format():
    return {
        'address_components': {
            'AddressNumber': '123',
            'StreetName': 'main',
            'StreetNamePostType': 'st',
            'PlaceName': 'chicago',
            'StateName': 'il',
        },
        'address_type': 'Street Address'
    }
