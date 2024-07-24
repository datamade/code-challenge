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
        request_params = request.query_params
        d = {'payload': '', 'errors': ''}
        try:
            if 'address' in request_params:
                try:
                    d['payload'] = self.parse(request_params['address'])
                except usaddress.RepeatedLabelError:
                    d['errors'] = 'Repeated Labels'
        except ValueError:
            d['errors'] = 'Fill a valid address'
        return Response(d)

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        if address == "":
            raise ValueError("Parse again")
        (address_components, address_type) = usaddress.tag(address)
        return address_components, address_type
