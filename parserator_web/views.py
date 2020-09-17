import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'
    # print("************************", flush=True)
    # print("Home")
    # print("************************")


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        address = request.GET['address']
        address = self.parse(address)

        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        return Response(address[0])

    def parse(self, address):

        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        # return address_components, address_type

        address = usaddress.tag(address)
        address_type = address[1]
        address_components = dict(address[0])

        return address_components, address_type
        


# Helpers
def create_address_components(address):
    place_names = []
    street_names = []

    

    # AddressNumber, StreetName, StreetNamePostType, PlaceName, StateName

    for i in address:
        if (i[1] == 'AddressNumber'): address_number = i[0]
        if (i[1] == 'StreetName'): street_names.append(i[0])
        if (i[1] == 'StreetNamePostType'): street_name_post_type = i[0]
        if (i[1] == 'StateName'): state_name = i[0]
        if (i[1] == 'PlaceName'): place_names.append(i[0])
    
    # if element contains more than one word like 'San Jose'
    place_name = (' ').join(place_names)
    street_name = (' ').join(street_names)

    return address



 

   
