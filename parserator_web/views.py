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
        input_string = request.GET["address"]
        try:
            address_components, address_type = self.parse(input_string)

            return Response({"input_string": input_string,
                             "address_components": address_components,
                             "address_type": address_type})
        except usaddress.RepeatedLabelError as err:
            return Response({"address_type": f"Error: {err=}"})

    def parse(self, address):
        address_components, address_type = usaddress.tag(address)
        return address_components, address_type
