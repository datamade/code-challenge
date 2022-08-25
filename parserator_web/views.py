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
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.

             # need to return: 
             # input_string: The string that the user sent
             # address_components: A dictionary of parsed components that comprise the address, in the format {address_part: tag} (returned by AddressParse.parse())
             # address_type: A string representing type of the parsed address (returned by AddressParse.parse())
        # Don't forget to handle strings that cannot be parsed and return errors! -- ParseError
        #Query params?? 

        # peel off addy from request - query params? 
        # call custom parse helper w addy
        # return a response w formatted parsed address 
        pprint(request)
        self.parse('123 Main Street Chicago, IL')

        return Response({}) 
    

    def parse(self, address):
       
        response =  usaddress.tag(address)
        pprint("printing parse method response")
        pprint(response)
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        return response.address_components, response.address_type
