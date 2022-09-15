import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer



class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        address = request.query_params.get("address")
        input_string = str(address)
        try:
            address_components, address_type = self.parse(input_string)
            return Response({
                'Address': input_string,
                'Address Type': address_type,
                'Address Components': address_components,
                }, status=200)
        except usaddress.RepeatedLabelError as e:
            return Response({'error': e.message,
            'Original String': e.original_string,
            'Parsed String' : e.parsed_string
            }, status=400)


    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        address_components, address_type = usaddress.tag(address)[0], usaddress.tag(address)[1]
        return address_components, address_type

        
