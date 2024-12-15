from django.shortcuts import render
from rest_framework import viewsets
from .models import InventoryItem
from .serializers import InventoryItemSerializer, UserSerializer
from django.contrib.auth.models import User

# Create your views here.

class InventoryItemViewSet(viewsets.ModelViewSet):

    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
