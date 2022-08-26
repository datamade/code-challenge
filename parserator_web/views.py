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
        # request uses: https://www.django-rest-framework.org/api-guide/requests/

        # Parse an address string using the
        # parse() method and return the parsed components to the frontend.
        # address_components, address_type = self.parse(request)

        input_address = request.query_params['address']
        address_components = []
        address_type = "Test Type"
        
        # TODO handle invalid input
        
        return Response({
            'input_string': input_address,
            'address_components': address_components,
            'address_type': address_type
        })

    def parse(self, address):
        # Returns the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        parse_result = usaddress.tag(address)
        address_components = parse_result[0]
        address_type = parse_result[1]
        return address_components, address_type
