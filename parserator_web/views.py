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
        # get address query parameter from request
        address = request.query_params.get('address', None)

        # ParseError for no address being provided
        if not address:
            raise ParseError(detail="No valid address provided")

        # parse the address with parse method
        try:
            # call parse method to return:
            # address_components-- a dict of parsed address components
            # address_type-- string representing the type of address
            address_components, address_type = self.parse(address)

        except ParseError as e:
            # ParseError returns an error message -- RepeatedLabelError can cause this
            return Response({'error': str(e)}, status=400)

        # return components to the front end:
        # input_string-- the original address string sent by user
        return Response({
            'input_string': address,
            'address_components': address_components,
            'address_type': address_type
        })

    def parse(self, address):
        try:
            # use usaddress to parse each component of the string
            # usaddress.tag() returns tuple
            # tuple includes:
            # address_components-- key is address part and value is tag
            # address_type-- string representing the type of address
            address_components, address_type = usaddress.tag(address)
            return address_components, address_type
        except usaddress.RepeatedLabelError as e:
            # raise usaddress.RepeatedLabelError when component cannot
            # be uniquely labeled/ duplication of type
            # raise ParseError with error message to handle this in API response
            raise ParseError(detail=f"Error in parsing address: {str(e)}")
