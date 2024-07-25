import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError

# Define a class to render the home template
class Home(TemplateView):
    template_name = 'parserator_web/index.html'

# Define a class to handle API requests for address parsing
class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    # Handles the GET requests
    def get(self, request):
        # Get the 'address' parameter from the request
        input_string = request.GET.get("address")
        
        # If the address parameter is missing, raise a ParseError
        if not input_string:
            raise ParseError(detail="Address parameter is missing.")
        
        try:
            # Parse the address using the 'parse' method
            components, address_type = self.parse(input_string)
            
            # Convert the parsed components dictionary to a list of tuples
            address_components = [(comp, components[comp]) for comp in components]
            
            # Return a JSON response with the parsed address details
            return Response({
                "input_string": input_string,
                "address_components": address_components,
                "address_type": address_type
            })
        except usaddress.RepeatedLabelError:
            # If the address parsing fails, return an error response
            return Response({"error": "This address failed to parse"}, status=400)

    # Define a method to parse the address using the 'usaddress' library
    def parse(self, address):
        # Use the 'usaddress.tag' function to parse the address
        return usaddress.tag(address)
