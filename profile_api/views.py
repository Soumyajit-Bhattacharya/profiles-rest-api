from django import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profile_api import models, permissions, serializers
from rest_framework.authentication import TokenAuthentication



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
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle partial update"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """deletes object"""
        return Response({'method': 'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'uses actions (List, create, retrieve, partial_update, update)',
            'Automatically maps urls using routers',
            'provides more functionality',
        ]

        return Response({"message": "hello", "a_viewset": a_viewset})

    def create(self,request):
        """Createanew hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello{name}!'
            return Response({'message':message})
        else:    
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
       )

    def retrieve(self, request, pk=None):
        """handles getting object by id"""
        return Response({'http-method': 'GET'})

    def update(self, request, pk=None):
        """updates object"""
        return Response({'http-method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """partial update"""
        return Response({'http-method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Deletes"""
        return Response({'http-method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class= serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)