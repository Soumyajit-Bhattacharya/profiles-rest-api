from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of API view features"""
        an_apiview = [
            'uses http methods',
            'gives most control',
            'maps manually',
        ]

        return Response({'messgae': 'hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get(name)
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )