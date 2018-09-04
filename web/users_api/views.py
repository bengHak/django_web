from django.shortcuts import render

from rest_framework import viewsets
from .serializers import UserProfileSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    