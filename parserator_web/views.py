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
        input_address = request.GET.get('address', "")
        if input_address == "":
            raise ParseError("Non-blank address query param must be provided.")

        try:
            address_components, address_type = self.parse(input_address)
            return Response({
                'input_string': input_address,
                'address_components': address_components,
                'address_type': address_type
            })
        except Exception as e:
            # TODO better handle parse error?
            raise ParseError(e)

    def parse(self, address):
        parse_result = usaddress.tag(address)
        address_components = parse_result[0]
        address_type = parse_result[1]
        return address_components, address_type
