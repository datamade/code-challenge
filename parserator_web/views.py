import usaddress
import json
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
        #retreive the address portion of the get query
        address_raw = request.query_params['address']
        #pass the string to the parse method and return the results as a json response to the get request
        return Response({AddressParse.parse(self, address_raw)})

    def parse(self, address):
        
        #parse the python dict to json
        address_components = json.dumps(usaddress.tag(address), indent=2)
        return address_components
 