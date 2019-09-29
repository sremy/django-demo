from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, GenericSerializer
from rest_framework.decorators import api_view

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ManualView(APIView):
    def get(self, request: Request, format=None):
        print("request.query_params: " + str(request.query_params))
        print("request.POST: " + str(request.POST))
        return Response([1, 3])


class GenericView(generics.GenericAPIView):
    serializer_class = GenericSerializer

    def get(self, request: Request, format=None):
        return Response({'key': 'GET'})

    #@api_view(['POST'])
    def post(self, request: Request, format=None):
        #name = request.POST.get('name')
        return Response({'key': 'POST'})