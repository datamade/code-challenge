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
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        user_input = request.query_params['input_string']
        if user_input:
            parsed = self.parse(user_input)
            response_data = {
                "input_string": user_input,
                "address_components": parsed[0],
                "address_type": parsed[1]
            }
        else:
            # Return error if user did not provide a string
            raise ParseError(detail="Please provide a value to parse")
        return Response(response_data)

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try:
            address_components, address_type = usaddress.tag(address)
        except usaddress.RepeatedLabelError:
            raise ParseError(detail="Unable to parse this value due to repeated labels.")

        return address_components, address_type
