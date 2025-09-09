from django.shortcuts import render
from rest_framework import viewsets, filters, status
from gascontrolproject.models import Condominio, Torres
from django_filters.rest_framework import DjangoFilterBackend
from gascontrolproject.serializer import CondominioSerializer, TorresSerializer

class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all().order_by('?')
    serializer_class = CondominioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'local']
    


class TorresViewSet(viewsets.ModelViewSet):
    queryset = Torres.objects.all().order_by('?')
    serializer_class = TorresSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    
