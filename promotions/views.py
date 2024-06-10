from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .serializers import PromotionsSerializers
# Create your views here.

class PromotionViewset(viewsets.ModelViewSet):
    queryset = models.Promotions.objects.all()
    serializer_class = PromotionsSerializers