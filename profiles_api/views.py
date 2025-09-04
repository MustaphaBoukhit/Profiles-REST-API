from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from rest_framework import generics

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview=[
            'Uses HTTP methods as function (get, post, fetch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most contro over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:  
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """
    serialier_class  = serializers.HelloSerializer
    def list(self, request):
        """return a hello message """
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'Hello there', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validate_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serialier.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Handle getting an object by it's ID """
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object """
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of  an object """
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing  an object """
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    # , here is intentionally added to allow python interpret it's intended to be a tuple and nmot a single item
    filter_backends = (filters.SearchFilter,) 
    search_fields = ('name', 'email',)