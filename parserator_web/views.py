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
        address_string = request.query_params.get('address', None)
        if not address_string:
            raise ParseError(detail="No address provided")

        address_components, address_type = self.parse(address_string)

        if address_components is None:
            raise ParseError(detail="Invalid address format")

        return Response({
            "input_string": address_string,
            "address_components": address_components,
            "address_type": address_type
        })

    def parse(self, address):
        try:
            parsed_address, address_type = usaddress.tag(address)
            return parsed_address, address_type
        except usaddress.RepeatedLabelError:
            return None, None
