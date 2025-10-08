from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here

class HelloApiView(APIView):
    """Test api views"""
    def get(self,request, format=None):

        """returns the list of featurs of the api"""
        an_apiview=[
            "uses https methods as function ( get, post, patch, put, fetch)"
            "is similer to a django view",
            "gives the most control over the application logic ",
            "is mapped manually to urls "
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    