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
        :param self: object - AddressParse class object
        :param request: string - unparsed address string from user
        :return response_data: object with input_string (string) from user,
        address_components (dict) from parsed_result, and address_type (string)
        from parsed_result
        :return ParseError - error if invalid input_string
        """

        input_string = request.query_params['input_string']

        try:
            parsed_result = self.parse(input_string)
            response_data = {
                "input_string": input_string,
                "address_components": parsed_result[0],
                "address_type": parsed_result[1]
            }
        except ParseError as error:
            raise ParseError(detail=error)

        return Response(response_data)

    def parse(self, address):
        """
        :param self: object - AddressParse class object
        :param address: string - unparsed address string from user
        :return address_components: dict - parsed address
        :return address_type: string - address type
        :return ParseError - returns error for invalid strings
        """

        try:
            tag = usaddress.tag(address)
            address_components = dict(tag[0])
            address_type = tag[1]
            return address_components, address_type
        except usaddress.RepeatedLabelError as error:
            raise ParseError(detail=error)
