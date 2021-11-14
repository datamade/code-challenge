import usaddress
from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest
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
        address = self.parse(request.GET["address"])
        if address != "Repeated Label Error":
            return Response(
                {
                    "input_string": request.GET["address"],
                    "address_components": address[0],
                    "address_type": address[1]
                }
            )
        else:
            return HttpResponseBadRequest("Repeated Label Error")

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try:
            tagged_address = usaddress.tag(address)
            address_components = tagged_address[0]
            address_type = tagged_address[1]
            return address_components, address_type
        except usaddress.RepeatedLabelError:
            return "Repeated Label Error"
