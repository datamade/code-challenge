import pytest
from rest_framework.test import APIRequestFactory
from django.urls import reverse
import usaddress


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    address_check = usaddress.tag(address_string)
    url = reverse('address-parse')
    factory = APIRequestFactory()
    request = factory.get(url, {"address": address_string})
    request = request.get_full_path()
    response = client.get(request)
    if response.status_code != 200:
        pytest.fail('Incorrect status code from API')
    data = response.data
    if data['input_string'] != address_string:
        pytest.fail("Input string did not match")
    if data['address_components'] != address_check[0]:
        pytest.fail("Address components did not match")
    if data['address_type'] != address_check[1]:
        pytest.fail("Address type did not match")


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    url = reverse('address-parse')
    factory = APIRequestFactory()
    request = factory.get(url, {"address": address_string})
    request = request.get_full_path()
    response = client.get(request)
    if response.status_code != 200:
        pytest.fail('Incorrect status code from API')
    data = response.data
    if data['errorType'] != "RepeatedLabelError":
        pytest.fail("Did not give correct error")
