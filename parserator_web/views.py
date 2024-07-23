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
        address = request.query_params.get('address', None)
        if not address:
            raise ParseError("No address provided")

        address_components, address_type = self.parse(address)

        return Response({
            'input_string': address,
            'address_components': address_components,
            'address_type': address_type
        })

    def parse(self, address):
        try:
            parsed_address = usaddress.tag(address)
            address_components = parsed_address[0]
            address_type = parsed_address[1]
        except usaddress.RepeatedLabelError as e:
            raise ParseError("Invalid address")

        return address_components, address_type