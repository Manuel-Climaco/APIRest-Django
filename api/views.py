from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CatalogoSerializer
from .models import Catalogo
# Create your views here.

class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo.objects.all()
    serializer_class = CatalogoSerializer
