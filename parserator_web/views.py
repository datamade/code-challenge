import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError
from urllib.parse import unquote


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        address_query_param = request.GET.get('address', "")
        if address_query_param == "":
            raise ParseError("Non-blank address query param must be provided.")
        input_string = unquote(address_query_param)

        try:
            address_components, address_type = self.parse(input_string)
            return Response({
                'input_string': input_string,
                'address_components': address_components,
                'address_type': address_type
            })
        except Exception as e:
            raise ParseError(e)

    def parse(self, address):
        parse_result = usaddress.tag(address)
        address_components = parse_result[0]
        address_type = parse_result[1]
        return address_components, address_type
