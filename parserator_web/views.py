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
        print(request)
        address = request.data["address"]

        response = self.parse(address)
        if response["status"] == 200:
            return Response({"status": response["status"],
                             "input_string": address,
                             "address_components": response["address_components"],
                             "address_type": response["address_type"]})
        return Response({"status": 400,
                         "input_string": response["original_string"],
                         "address_components": response["parsed_string"],
                         "address_type": "Unknown"})

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress

        # https://usaddress.readthedocs.io/en/latest/
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses
        try:
            address_components, address_type = usaddress.tag(address)
        except usaddress.RepeatedLabelError as e:
            return Response({"status": 400,
                             "parsed_string": e.parsed_string,
                             "original_string": e.original_string})

        return Response({"status": 200,
                         "address_components": address_components,
                         "address_type": address_type})
