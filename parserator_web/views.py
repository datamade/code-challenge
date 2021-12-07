import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


ADDRESS_KEY = 'address'
INPUT_STRING_KEY = 'input_string'
ADDR_COMPONENTS_KEY = 'address_components'
ADDR_TYPE_KEY = 'address_type'


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:

            # Pull input string from request and parse it
            input_string = request.GET[ADDRESS_KEY]
            address_components, address_type = self.parse(input_string)

            return Response({
                    INPUT_STRING_KEY: input_string,
                    ADDR_COMPONENTS_KEY: address_components,
                    ADDR_TYPE_KEY: address_type
                })
        except usaddress.RepeatedLabelError as e:
            raise ParseError(e)

    def parse(self, address):
        return usaddress.tag(address)
