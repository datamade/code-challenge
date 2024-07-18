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
        input_string = request.GET.get("address")
        try:
            components, address_type = self.parse(input_string)
            address_components = []
            for comp in components:
                address_components.append((comp, components[comp]))
            return Response({"input_string": input_string,
                             "address_components": address_components,
                             "address_type": address_type})
        except ParseError:
            return Response({"error": "This address failed to parse"}, status=400)

    def parse(self, address):
        # We'll let our library to the heavy lifting here
        # And we'll re-throw the usaddress exception as a ParseError
        try:
            return usaddress.tag(address)
        except usaddress.RepeatedLabelError:
            raise ParseError
