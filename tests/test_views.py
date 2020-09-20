import pytest
import usaddress


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    parsed_address = usaddress.tag(address_string)

    assert type(parsed_address) is tuple
    
    
def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st' 
    with pytest.raises(usaddress.RepeatedLabelError):
        usaddress.tag(address_string)

