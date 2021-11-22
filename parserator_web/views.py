import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from rest_framework.exceptions import ParseError # for bad parse?
from rest_framework import status


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]
    #parser_classes = [JSONParser] may need this for later

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        #if request.method == 'GET':
        #print("im here")
        #print("request data: ", request)
        #print("here is the request data: ", str(request))
        #a, b = self.parse(request.data)
        #if a == None or b == None:
            #return Response({'data' : {}, 'status' : status.HTTP_406_NOT_ACCEPTABLE})
        #    return Response({'data' : {},})
        #return Response({'input_string': request.data, 'address_components': a, 'address_type': b}) 
        print("made it to api/parse")
        #print(request.data.value)
        a,b = self.parse("123 Main St. Suite 100 Chicago, IL")
        return Response({"input_string": "123 Main St. Suite 100 Chicago, IL", "address_components": a, "address_type": b}, status=status.HTTP_200_OK)   

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        print("here is what im working with: ", address)
        try: 
            address_components = usaddress.tag(address)
        except Exception as e: 
            print(e, "that's the shit that happened")
            return e, {}
        #except:  #usaddress.RepeatedLabelError as e: <- use as better exception?  could return diff things print('Warn: Can\'t parse mailing address. Falling back to residential ({})'.format(e.parsed_string)) <- have some class that raises the shit.
        #    address_components = None
        #    address_type = None
        #    print("the first function is not even working")
        #    return address_components, address_type
            #todo: put in some more stuff on all the possible errors 
        return address_components[0], address_components[1]
