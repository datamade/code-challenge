import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError
from rest_framework import status


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        """Returns the string the user sent, the parsed address
        components and the address type if the string is a valid address"""
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.

        # Get the unparsed address from JSON object query
        input_string = request.query_params['address']

        try:

            # Get address components using .parse() method
            address_components, address_type = self.parse(input_string)

            # Return a dictionary object
            return Response({
                'input_string': input_string,
                'address_components': address_components,
                'address_type': address_type
            })

        except:

            # Return the expected dictionary object, but include error info
            return Response({
                'input_string': input_string,
                'address_components': '',
                'address_type': 'Invalid',},
                status=status.HTTP_400_BAD_REQUEST)

    def parse(self, address):
        """Returns parsed components and address type of a given address 
        using usaddress"""

        # Use .tag() from usaddress to parse address
        address_components, address_type = usaddress.tag(address)

        # Return address_components as OrderedDict and address_type as Str
        return address_components, address_type
