from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
# from rest_framework.exceptions import ParseError
import usaddress


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        try:
            input_string = request.GET.get("address")
            address_components, address_type = AddressParse.parse(
                self, address=input_string)
            return Response({
                "input_string": input_string,
                "address_components": address_components,
                "address_type": address_type
            })
        except Exception as e:
            return Response({
                "error": e.message,
                "errorType": str(type(e).__name__)
            })

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        address_components = usaddress.tag(address)[0]
        address_type = usaddress.tag(address)[1]
        return address_components, address_type
