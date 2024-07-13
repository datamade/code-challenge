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

# Gets address string from query params, parses it, and returns response
    def get(self, request):
        input_string = request.query_params.get('address', None)
        if not input_string:
            raise ParseError('No address provided')

        try:
            response = self.parse(input_string)
        except Exception as e:
            raise ParseError(e)

        response_data = {
            'input_string': input_string,
            'address_components': response[0],
            'address_type': response[1]
        }
        return Response(response_data)

# Parses address string, returns ordered dict of address components and address type
    def parse(self, address):
        address_components, address_type = usaddress.tag(address)
        return address_components, address_type
