from django.shortcuts import render
from .serializers import NamelistSerializers
from rest_framework.generics import ListCreateAPIView
from .models import Namelist

class apiView(ListCreateAPIView):
    queryset=Namelist.objects.all()
    serializer_class = NamelistSerializers
