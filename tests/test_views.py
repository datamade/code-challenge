import pytest
from pprint import pprint
from urllib.parse import urlencode #to encode address string into a query string for server
from django.urls import reverse

HTTP_406_NOT_ACCEPTABLE = 406
HTTP_200_OK = 200


@pytest.mark.django_db
def test_api_parse_succeds(client):
    # Send a request to the API and confirms that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    query = {'input_string': address_string}
    query_string = urlencode(query)
    url = reverse('address-parse') + '?' + query_string
    response = client.get(url) 
    assert response.status_code == HTTP_200_OK

@pytest.mark.django_db
def test_api_parse_raises_error(client):
    # The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    query = {'input_string': address_string}
    query_string = urlencode(query)
    url = reverse('address-parse') + '?' + query_string
    response = client.get(url) 
    print(response.status_code)
    assert response.status_code == HTTP_406_NOT_ACCEPTABLE