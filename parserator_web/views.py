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
        input_string = request.GET["address"]

        try:
            # need to return: 
             # input_string: The string that the user sent
             # address_components: A dictionary of parsed components that comprise the address, in the format {address_part: tag} (returned by AddressParse.parse())
             # address_type: A string representing type of the parsed address (returned by AddressParse.parse())
         address_components, address_type = self.parse(input_string)
         return Response({'input_string':input_string, 'address_components':address_components, 'address_type':address_type})

        except usaddress.RepeatedLabelError:
            #not sure how to implement ParseError, maybe add Response? 
            return ParseError


    def parse(self, address):
       # Use usaddress parse method to get components and type
        address_components, address_type =  usaddress.tag(address)

        return address_components, address_type
