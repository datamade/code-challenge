import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def find_repeat(self, parsed_address) -> str:
        """Finds the repeated label in a parsed address.

        Args:
            parsed_address (str): Parsed address.

        Returns:
            str: Repeated label.
        """
        labels = []
        for _, label in parsed_address:
            if label in labels:
                return label
            labels.append(label)

    def get(self, request) -> Response:
        """Parses an address string using the parse() method and returns the
        parsed components to the frontend.

        Args:
            request (request): Django request object.

        Returns:
            Response: JSON response.
        """
        address: str = request.GET.get('address')

        try:
            address_components, address_type = self.parse(address)
            response = Response({
                'input_string': address,
                'address_components': address_components,
                'address_type': address_type,
                'error:': "",
            }, status=status.HTTP_200_OK)
        except ParseError:
            response = Response({
                'input_string': address,
                'address_components': {},
                'address_type': "",
                'error': "Address cannot be empty",
            }, status=status.HTTP_400_BAD_REQUEST)
        except usaddress.RepeatedLabelError:
            response = Response({
                'input_string': address,
                'address_components': {},
                'address_type': "",
                'error': "Cannot parse address with repeated labels",
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = Response({
                'input_string': address,
                'address_components': {},
                'address_type': "",
                'error': f"Unknown error: {str(e)}",
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response

    def parse(self, address) -> tuple:
        """Returns parsed components of a given address using
        usaddress: https://github.com/datamade/usaddress

        Args:
            address (str): Address string.

        Raises:
            ValueError: Empty address string.
            ValueError: Address string contains repeated labels.
            e: Unknown error.

        Returns:
            tuple: Address components and address type.
        """
        address_components: list = []
        address_type = None

        if not address:
            raise ParseError("The address cannot be empty")

        try:
            parsed_address: tuple = usaddress.tag(address)
            address_components: dict = parsed_address[0]
            address_type: str = parsed_address[1]
        except usaddress.RepeatedLabelError as e:
            raise e
        except Exception as e:
            raise e
        return address_components, address_type
