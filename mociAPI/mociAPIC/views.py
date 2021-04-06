
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render

from .models import encuesta_1, UserProfile

from .serializers import  encuestaSerializer, usuarioSerializer

class encuestaViewSet(viewsets.ModelViewSet):
    serializer_class = encuestaSerializer
    queryset = encuesta_1.objects.all()

class usuarioViewSet(viewsets.ModelViewSet):
    serializer_class = usuarioSerializer
    queryset = UserProfile.objects.all()
