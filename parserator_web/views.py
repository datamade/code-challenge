import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError
from rest_framework.decorators import api_view


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):

        input_string = request.data['address']
        try:
            address_components, address_type = self.parse(request.data['address'])
            return_data = {
                'input_string': input_string,
                'address_components': address_components,
                'address_type': address_type
            }
            return Response({'return_data': return_data})
            
        except ParseError:
            return ParseError


    def parse(self, address):

        address_components = usaddress.parse(address)
        address_tagged = usaddress.tag(address)
        address_type = address_tagged[-1]
        
        return address_components, address_type
