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
        raw_address = request.query_params.get('address')

        parsed_address = self.parse(raw_address)
        status_code = 200
        if isinstance(parsed_address, tuple):
            address_components, address_type = parsed_address
            response = {
                'status': 'success',
                'input_string': raw_address,
                'address_components': address_components,
                'address_type': address_type,
            } 
        elif isinstance(parsed_address, ParseError):
            status_code = 400
            response = {
                'status': 'error',
                'error': parsed_address.detail,
            }
            
        return Response(data=response, status=status_code)

    def parse(self, address):
        '''Takes an address (string) and uses usaddress module to get a parsed address (dict) and address type (string)'''
        try:
            # tuple(<parsed address>, <type of address>)
            return usaddress.tag(address)
        except: 
            return ParseError(f"Error: {address} is not a valid address")