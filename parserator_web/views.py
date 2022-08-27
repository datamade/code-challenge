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
        address = request.query_params["address"]

        response = self.parse(address)
        if response.status_code == 200:
            return Response({"input_string": address,
                             "address_components": response.data["address_components"],
                             "address_type": response.data["address_type"]},
                            status=response.status_code)
        return Response({"input_string": response.data["original_string"],
                         "address_components": response.data["parsed_string"],
                         "address_type": "Unknown"},
                        status=response.status_code)

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress

        # https://usaddress.readthedocs.io/en/latest/
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses
        try:
            address_components, address_type = usaddress.tag(address)
        except usaddress.RepeatedLabelError as e:
            return Response({"parsed_string": e.parsed_string,
                             "original_string": e.original_string},
                            status=400)

        return Response({"address_components": address_components,
                         "address_type": address_type},
                        status=200)
