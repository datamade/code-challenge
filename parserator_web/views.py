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
        input_string = request.GET['address']
        try:
            address_components, address_type = self.parse(input_string)
        except usaddress.RepeatedLabelError:
            raise ParseError(detail='Unable to parse this value due to repeated labels. Please correct and resubmit')

        return Response({
            'input_string': input_string,
            'address_components': address_components,
            'address_type': address_type
        })

    def parse(self, address):
        address_parse = usaddress.tag(address)
        return address_parse
