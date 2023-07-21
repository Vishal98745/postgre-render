from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class student(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
