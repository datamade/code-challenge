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
        try:
            address_components, address_type = self.parse(request.GET['address'])
            return Response({"input_string": request.GET['address'],
                             "address_components": address_components,
                             "address_type": address_type})
        except usaddress.RepeatedLabelError as e:
            raise ParseError(detail=e)

    def parse(self, address):
        parsed_addr = usaddress.tag(address)
        address_components = dict(parsed_addr[0])
        address_type = parsed_addr[-1]
        return address_components, address_type