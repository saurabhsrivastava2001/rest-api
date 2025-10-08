# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


# Create your views here

class HelloApiView(APIView):
    """Test api views"""
    serializer_class = serializers.HelloSerializer

    def get(self,request, format=None):

        """returns the list of featurs of the api"""
        an_apiview=[
            "uses https methods as function ( get, post, patch, put, fetch)"
            "is similer to a django view",
            "gives the most control over the application logic ",
            "is mapped manually to urls "
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """create hello message to the passed name"""
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message= f'hello there {name}'
            return Response({'message':message})
        else :
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
        
    def put( self, request,pk=None):
        """Handle updating an object""" # replaces it rather that updating 
        return Response({'method':'PUT'})
    

    def patch(self,request,pk=None):
        " handle the partial update of an object" 
        return Response( {'method':'PATCH'})
    
    def delete( self, request, pk=None):
        return Response( {'method':'DELETE'})