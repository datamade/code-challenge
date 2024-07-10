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
        input_string = request.GET.get("address", "")
        if not input_string:
            raise ParseError(detail="No address given")
        
        address_components, address_type = self.parse(input_string)
        return Response({
            "input_string": input_string,
            "address_components":address_components,
            "address_type":address_type
        })

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try:
            address_components, address_type = usaddress.tag(address)
            address_components = {k: v for k, v in address_components.items()}
            return address_components, address_type
        except usaddress.RepeatedLabelError as e:
            raise ParseError(detail=str(e))
