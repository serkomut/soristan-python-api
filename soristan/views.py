from django.shortcuts import render
from rest_framework import viewsets
from soristan.models import User
from soristan.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer