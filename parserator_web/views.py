import usaddress
from pprint import pprint
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
        input_string = request.query_params['address']
        try:
         address_components, address_type = self.parse(input_string)
         return Response({'input_string':input_string, 'address_components':address_components, 'address_type':address_type})

        except usaddress.RepeatedLabelError as e:
            print('error', e)
            return Response({'error': "Sorry, we couldn't parse this address. Please check your address and try again!"})

    def parse(self, address):
        address_components, address_type =  usaddress.tag(address)
        return address_components, address_type
