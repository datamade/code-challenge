import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError
from django.shortcuts import render


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        input_string = request.GET.get('address')
        address_components, address_type = self.parse(input_string)
        print({
            'input_string': input_string,
            'address_components': address_components,
            'address_type': address_type,
        })
        return render(request, 'parserator_web/index.html', {
            'input_string': input_string,
            'address_components': address_components,
            'address_type': address_type,
        })
        return Response({
            'input_string': input_string,
            'address_components': address_components,
            'address_type': address_type,
        })

    def parse(self, address: str):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try:
            address = address.strip()
            if len(address) == 0:
                address_components = "The string is Empty!"
            else:
                try:
                    input_string = usaddress.parse(address)
                    address_components = {}
                    for item in input_string:
                        if item in address_components.items():
                            address_components = "Unable to parse this value \
                                due to repeated labels!"
                            break
                        address_components[item[0]] = item[1]
                except ParseError:
                    address_components = "Unable to parse this value because \
                        of invalid address!"
        except AttributeError:
            address_components = "Empyt Address!"
        address_type = type(address_components)
        return address_components, address_type
