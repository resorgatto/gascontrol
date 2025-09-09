from django.shortcuts import render
from rest_framework import viewsets, filters, status
from gascontrolproject.models import Condominio, Torres
from django_filters.rest_framework import DjangoFilterBackend

class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all().order_by('?')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'local']

class TorresViewSet(viewsets.ModelViewSet):
    queryset = Torres.objects.all().order_by('?')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']