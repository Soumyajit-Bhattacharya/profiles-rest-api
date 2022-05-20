from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns list of API view features"""
        an_apiview = [
            'uses http methods',
            'gives most control',
            'maps manually',
        ]

        return Response({'messgae': 'hello', 'an_apiview': an_apiview})