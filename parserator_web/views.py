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
        address = request.query_params.get('address')
        if not address:
            raise ParseError("Address parameter is required")
        
        try:
            address_components, address_type = self.parse(address)
            return Response({
                'input_string': address,
                'address_components': address_components,
                'address_type': address_type
            })
        except usaddress.RepeatedLabelError as e:
            raise ParseError(f"Error parsing address: {str(e)}")

    def parse(self, address):
        """
        Parse the given address using usaddress.
        
        Args:
            address (str): The address string to parse.
        
        Returns:
            tuple: A tuple containing two elements:
                1. address_components (dict): The parsed address components.
                2. address_type (str): The type of address provided.
        """
        address_components, address_type = usaddress.tag(address)
        
        # Convert OrderedDict to regular dict for better JSON serialization
        address_components = dict(address_components)
        
        return address_components, address_type