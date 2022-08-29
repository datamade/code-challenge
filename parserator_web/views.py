import usaddress
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Set up base Exception response to use different http status
        # that way we can handle different error types and show them differently
        input_string = request.query_params["address"]
        try:
            address_components, address_type = self.parse(input_string)
        except usaddress.RepeatedLabelError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': e.message})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': e.message})
        return Response({'input_string': input_string,
                         'address_components': address_components,
                         'address_type': address_type})

    def parse(self, address):
        parsedTuple = usaddress.tag(address)
        address_components = parsedTuple[0]
        address_type = parsedTuple[1]
        return address_components, address_type
