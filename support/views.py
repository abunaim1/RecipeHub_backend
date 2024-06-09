from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

# Create your views here.



class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

    def perform_create(self, serializer):
        contact = serializers.save()
