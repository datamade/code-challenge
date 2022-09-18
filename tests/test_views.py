import json
import usaddress
import pytest
from django.urls import reverse
from rest_framework.test import APIRequestFactory

def visit_site(client, address_string):

    data = {'address': address_string}
    headers = {
        'method': 'POST',
        'headers': {
        'Content-Type': 'application/json'
        },
    }

    url = reverse('address-parse')
    response = client.post(url, data, headers=headers)

    return response

def test_api_parse_succeeds(client):

    address_string = '123 main st chicago il'
    
    response = visit_site(client, address_string)
    expected_response = {'return_data': 
            {
                'input_string': '123 main st chicago il',
                'address_components': [("123", "AddressNumber"),
                                       ("main", "StreetName"),
                                       ("st", "StreetNamePostType"),
                                       ("chicago", "PlaceName"),
                                       ("il", "StateName")],
                'address_type': 'Street Address'
            }
        }

    assert response.data['return_data']['input_string'] == expected_response['return_data']['input_string']
    assert response.data['return_data']['address_type'] == expected_response['return_data']['address_type']
    assert response.data['return_data']['address_components'] == expected_response['return_data']['address_components']


def test_api_parse_raises_error(client):

    address_string = '123 main st chicago il 123 main st'
    try:
        response = visit_site(client, address_string)
    except Exception as e:
        print(e)
        return e
        


    



    
