from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'hello', 'an_apiview':an_apiview})

    def post(self,request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """handle a partial update of an object"""
        return Response({'method':'PATCH'} )

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test api viewset"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'User actions (list, create, retrieve, update, partial_udpate)',
            'automatically maps to urls using routers',
            'provides more functionality with less code',
        ]
        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        """handle getting an object by its id"""
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """handle updating an object"""
        return Response({'http_method':'PUT'})
    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles using generic viewset which is modelviewset"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)