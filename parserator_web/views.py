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
        return Response({})

    def parse(self, address):
        """
        Given an address string, return the parsed components of the address.
        """
        try:
            address_components, address_type = usaddress.tag(address)
        except usaddress.RepeatedLabelError:
            raise ParseError(f'Failed to parse the string "{address}"')

        return address_components, address_type
