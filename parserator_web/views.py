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
        #Try to parse the address string, if there is an error, pass that message on to the client for handling via JS. 
        #Otherwise pass the restult onto the client

        #Possible improvments: catch various common errors (e.g. a blank input) and pass them back to the client without pinging the API first
        #also parse error messages into human-readable instructions (e.g. "too many numbers!") and pass them to the client
        try:
            result = AddressParse.parse(self,address=request.GET.get('address'))
        except:
            result = "error!"
        return Response(result)

    def parse(self, address):
        #The excerscise instructions directed me to use useaddress.parse(). However, that method doesn't seem return the address type.
        #Thus, I've used useaddress.tag() to get the address type and useaddress.parse() for the parts. That said, using just tag() 
        #to get the parts and the type would have also worked.
        
        get_type = usaddress.tag(address)
        address_parts = usaddress.parse(address)
        address_components = address_parts
        address_type = get_type[1]
        return address_components, address_type
