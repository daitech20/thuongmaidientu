from django.shortcuts import render
from apps.users.api.serializers import RegisterSerializer, CustomJWTSerializer
from apps.users.models import User
from rest_framework import generics, status
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer