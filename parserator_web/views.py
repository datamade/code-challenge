import json
import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        input = request.query_params['input']
        try:
            parsed_address = self.parse(input)
        except:
            return Response({
                'error': 'Invalid address',
                'message': 'We could not parse that address'
            })
        return Response({
            'input_string': input,
            'address_components': json.dumps(parsed_address[0]),
            'address_type': parsed_address[1]
        })
      

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        result = usaddress.tag(address)
        address_components = result[0]
        address_type = result[1]
        return address_components, address_type
