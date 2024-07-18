import usaddress
from django.views.generic import TemplateView
from http import HTTPStatus
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = "parserator_web/index.html"


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        """
        Extracts the address from the get request
        """
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.

        address = request.GET.get("address")
        try:
            parsed_address, address_type = self.parse(address)
            response = Response(
                {
                    "input_string": address,
                    "address_components": parsed_address,
                    "address_type": address_type,
                },
            )

        except usaddress.RepeatedLabelError:
            response = Response(
                {
                    "input_string": address,
                    "address_components": {},
                    "address_type": "",
                    "error": "Remove repeated labels before parsing",
                },
                status=HTTPStatus.BAD_REQUEST,
            )

        except ParseError as error:
            response = Response(
                {
                    "input_string": address,
                    "address_components": {},
                    "address_type": "",
                    "error": str(error),
                },
                status=HTTPStatus.BAD_REQUEST,
            )

        except Exception as error:
            response = Response(
                {
                    "input_string": address,
                    "address_components": {},
                    "address_type": "",
                    "error": f"Unknown error: {error}",
                },
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
            )

        return response

    def parse(self, address):
        """
        Uses the usaddress package to parse the address
        """
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress

        if not address:
            raise ParseError("Address can not be empty")

        # Catch error and raise it as ParseError
        parsed_address = usaddress.parse(address)
        address_type = usaddress.tag(address)

        address_components = {}

        for element in parsed_address:
            address_components[element[1]] = element[0]

        address_type = address_type[-1]

        return address_components, address_type
