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
        
        input_string = request.GET['address']
        address = self.parse(input_string)
        address_components = address[0]
        address_type = address[1]

        address_components, address_type = self.parse(input_string)

        return Response([input_string, address_components, address_type])

    def parse(self, address):

        address_to_parse = usaddress.tag(address)
        print(address_to_parse)
        address_components = dict(address_to_parse[0])
        address_type = address_to_parse[1]

        return address_components, address_type
        