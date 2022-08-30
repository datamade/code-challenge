import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError # why is this used?


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
        except:
            original_string, parsed_string, error_desc = self.parse(input_string)
            
            return Response({
                'Original String': original_string,
                'Parsed String': parsed_string,
                'Error Description': error_desc,
            }, status=400)


    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try:
            address_components, address_type = usaddress.tag(address)[0], usaddress.tag(address)[1]

        except usaddress.RepeatedLabelError as e:
            error_desc = "Not a valid address!"
            return e.original_string, e.parsed_string, error_desc

        return address_components, address_type
