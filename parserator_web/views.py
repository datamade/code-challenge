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
        address_components, address_type = self.parse(input_string)

        return Response([input_string, address_components, address_type])

    def parse(self, address):

        try:
            parsed_address = usaddress.tag(address)
            address_components = dict(parsed_address[0])
            address_type = parsed_address[1]
            
        except Exception as e:
            print(e.message, type(e))
            return

        return address_components, address_type
        
        