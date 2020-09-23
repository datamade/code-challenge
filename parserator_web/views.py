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
        try:
            input_string = request.data
            address_components, address_type = self.parse(input_string)

            if (address_components is None) or (address_type is None):
                return None
            else:
                content = (input_string, address_components, address_type)

        except ParseError:
            print("Malformed data")
            return None

        return Response(content)


    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress

        try:
            address_components, address_type = usaddress.tag(address)

        except usaddress.RepeatedLabelError as e:
            print(e.orginal_string, "is not a valid address for tagging")
            return None, None

        return address_components, address_type
