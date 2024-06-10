from django.shortcuts import render
from rest_framework import viewsets
from .models import Podcast
from .serializers import PodcastSerializers
# Create your views here.

class PodcastViewset(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializers
    