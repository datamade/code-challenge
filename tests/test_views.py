import pytest
from pprint import pprint



def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '3733 Southport Ave, Chicago, IL'
    pprint('About to call client')
    response = client.get(f"/api/parse/?address={address_string}")

    expected_response = {
        'input_string': address_string,
        'address_components': {'AddressNumber': '3733',
        'StreetName': 'Southport',
        'StreetNamePostType': 'Ave',
        'PlaceName': 'Chicago',
        'StateName': 'IL'
        },
        'address_type': 'Street Address'  
    }

    assert expected_response == response.json()
    # should expect to get back 
    # (OrderedDict([('AddressNumber', '123'),
    #               ('StreetName', 'Main'),
    #               ('StreetNamePostType', 'Street'),
    #               ('PlaceName', 'Chicago'),
    #               ('StateName', 'IL')]),
    #               'Street Address')


# def test_api_parse_raises_error(client):
#     # TODO: Finish this test. The address_string below will raise a
#     # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
#     address_string = '123 main st chicago il 123 main st'
#     pytest.fail()
