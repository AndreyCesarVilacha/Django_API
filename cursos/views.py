from django.shortcuts import render
from rest_framework import viewsets
from .models import Curso
from .serializers import CursoSerializer

class CursoView(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer