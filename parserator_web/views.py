import usaddress
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class Home(TemplateView):
    template_name = "parserator_web/index.html"


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        address = request.data.get("address")
        try:
            parsed_address, address_type = usaddress.tag(address)
            return Response(
                {
                    "status": "success",
                    "parsed": parsed_address,
                    "address_type": address_type,
                },
                status=status.HTTP_200_OK,
            )
        except usaddress.RepeatedLabelError as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, *args, **kwargs):
        return Response(
            {"message": "Send a POST request with an address to parse."},
            status=status.HTTP_200_OK,
        )
