from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from .models import Client,Company,ClientUsers
from .serializers import ClientSerializer,CompanySerializer,ClientUserSerializer


from rest_framework.permissions import IsAdminUser

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]

# Define other views with appropriate permissions as required

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUserViewSet(viewsets.ModelViewSet):
    queryset = ClientUsers.objects.all()
    serializer_class = ClientUserSerializer