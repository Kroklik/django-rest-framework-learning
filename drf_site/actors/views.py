from django.shortcuts import render
from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer

# Create your views here.

class ActorApiView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer