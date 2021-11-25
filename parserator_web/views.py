import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from pprint import pprint
#from rest_framework.exceptions import ParseError # for bad parse?
from rest_framework import status
import os
from django import db


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # Parses an address string using the
        # parse() method and return the parsed components to the frontend.
        a, b = self.parse(request.GET.get('input_string'))
        if b is None: 
            # parsing error
            return Response({'error_message' : a}, status = status.HTTP_406_NOT_ACCEPTABLE) 
        return Response({
                        "input_string": request.GET.get('input_string'), 
                        "address_components": a, "address_type": b
                        },
                        status=status.HTTP_200_OK)   

    def parse(self, address):
        # Returns the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try: 
            address_components = usaddress.tag(address)
        except Exception as e:
            return str(e), None
        return address_components[0], address_components[1]
