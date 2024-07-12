import usaddress
from usaddress import RepeatedLabelError
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
        """
        API endpoint to parse a U.S. address
        expects a string "address" query
        responds with JSON, like:
            {
                "input_string": "123 main street"
                "address_components": {"AddressNumber": "123", ...},
                "addres_type": "Street Address"
            }
        """
        form_data = request.query_params
        if ("address" not in form_data):
            raise ParseError

        input_string = form_data["address"]

        try:
            (address_components, address_type) = self.parse(input_string)
            response_object = {}
            response_object["input_string"] = input_string
            response_object["address_components"] = address_components
            response_object["address_type"] = address_type

            return Response(response_object)

        except RepeatedLabelError:
            error_message = "Repeated Label Error; check that address is correct"
            return Response(
                {"error": error_message}, status=status.HTTP_400_BAD_REQUEST
            )
        # TODO: Add except clauses for any other errors raised by usaddress

    def parse(self, address):
        """
        Parses a United States address string into its component parts,
        using usaddress: https://github.com/datamade/usaddress.

        -> address_components: OrderedDict, address_type: str
        """
        (address_components, address_type) = usaddress.tag(address)
        return address_components, address_type
