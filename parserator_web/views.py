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
        """
        API endpoint to handle requests to parse address strings.
        Returns
        - input string,
        - parsed address (tagged by component),
        - address type as JSON
        Except when parse() passes a ReapetedLabelError
        """
        input_string = request.GET.get('address')
        try:
            tagged_address, address_type = self.parse(input_string)
            return Response({
                "status": "success",
                "tagged_address": tagged_address,
                "address_type": address_type,
                "input_string": input_string,
            })
        except usaddress.RepeatedLabelError as rle:
            return Response({
                "status": "repeatedLabelError",
                "original_string": rle.original_string,
                "parsed_string": rle.parsed_string,
            })

    def parse(self, input_string):
        """
        passes input_string to usaddress.tag(), returning a tuple containing:
        - parsed and tagged string as OrderedDict: {'AddressNumber': '123'}
        - a string describing the address type
        """
        address_components, address_type = usaddress.tag(input_string)
        return address_components, address_type
