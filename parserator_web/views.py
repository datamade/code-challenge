import usaddress
from typing import Tuple, Dict
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

class Home(TemplateView):
    template_name = "parserator_web/index.html"


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request) -> Response:


        # Obtain request from search
        address = request.query_params.get("address", "")
        if not address:
            logging.info("Address not received")
            return Response({"error": "No address provided"}, status=400)

        # Parse input address
        try:
            address_components, address_type = self.parse(address)
        except usaddress.RepeatedLabelError as e:
            logging.info(f"Parsing address {address} not succesful: {e}")
            return Response(
                {"error": f"Not possible to parse address: {str(e)}"},
                status=400,
            )
        except ParseError as e:
            logging.info(f"Parsing address {address} not succesful: {e}")
            return Response(
                {"error": f"Not possible to parse address: {str(e)}"},
                status=400,
            )
        except Exception as e:
            return Response(
                {"error": f"Not possible to parse address: {str(e)}"},
                status=400,
            )

        # Compile results
        data = {
            "input_string": address,
            "address_components": address_components,
            "address_type": address_type,
        }

        return Response(data)

    def parse(self, address: str) -> Tuple[Dict, str]:
        """
        From a valid string, it returns the parsed address components and address 
        type using the usaaddress library
        Input: 
        - address (str): Address to be parsed
        Return: 
        - address_componenets (dict): Dictionary with tag as the key and its 
        corresponding value as the value
        - address_type (str): Type of address
        """

        address_components, address_type = usaddress.tag(address)
        return address_components, address_type
