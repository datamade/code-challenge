import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        address_request = request.query_params.get('address')

        # Use the parse() method to return both the type and parts of an address
        parsed_request = AddressParse.parse(self, address_request)
        address_parts = parsed_request[0]
        address_type = parsed_request[1]

        return Response({'requested_address': address_request,
                         'address_parts': address_parts,
                         'address_type': address_type})

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try:
            parsed_address = usaddress.tag(address)
            address_components = parsed_address[0]
            address_type = parsed_address[1]
        # When this error is thrown, store the message in address_components
        # to be later displayed to the user
        except usaddress.RepeatedLabelError:
            address_components = "Multiple areas of this address have the same label." \
                " It is likely that either (1) the input string is not a valid address,"\
                " or (2) some tokens were labeled incorrectly."
            address_type = 'Error'

        return address_components, address_type
