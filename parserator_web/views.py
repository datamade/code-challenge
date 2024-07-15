import usaddress
from usaddress import RepeatedLabelError
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    """
    A view class that represents a parsed US address.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request):
        """
        Turns a request into an API response containing a parsed US address.

        Args:
            request (HTTP request): Input string containing an address to be parsed.

        Raises:
            ParseError: Checks that query_params are valid otherwise raises ParseError.

        Returns:
            HTTP response: A response object containing input_string, address_components,
            and address_type.
        """
        # Address string passed in via request params
        address = request.query_params.get('address')
        # Check that request params have valid structure
        if 'address' not in request.query_params:
            raise ParseError
        # Create the response values
        try:
            address_components, address_type = self.parse(address)
            return Response({
                'input_string': address,
                'address_components': address_components,
                'address_type': address_type
            })
        # Handle exceptions and errors
        except (RepeatedLabelError, TypeError):
            return Response({'RepeatedLabelError': 'Unable to parse this value due to '
                            'repeated labels. Our team has been notified of the error.'},
                            status=400)
        except Exception as e:
            return Response({'Error': 'Error ' + e}, status=400)

    def parse(self, address):
        """
        Method for parsing US addresses via the usaddress module.

        Args:
            address (string): The address to be parsed.

        Returns:
            Object: parsed address_components and address_type.
        """
        address_components, address_type = usaddress.tag(address)
        return address_components, address_type
