from django.shortcuts import render
from rest_framework import viewsets
from .models import source
from .serializers import sourceSerializer

# Create your views here.
class sourceViewSet(viewsets.ModelViewSet):
      queryset = source.objects.all()
      serializer_class = sourceSerializer
