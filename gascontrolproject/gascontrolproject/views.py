from django.shortcuts import render
from rest_framework import viewsets, filters, status
from gascontrolproject.models import Condominio, Torres, Apartamento, Pessoa, Hidrometro, Leitura
from django_filters.rest_framework import DjangoFilterBackend
from gascontrolproject.serializer import CondominioSerializer, TorresSerializer, ApartamentoSerializer, PessoaSerializer, HidrometroSerializer, LeituraSerializer
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
    ordering_fields = ['identificacao']
    search_fields = ['identificacao']
    
    
class ApartamentoViewSet(viewsets.ModelViewSet):
    queryset = Apartamento.objects.all().order_by('?')
    serializer_class = ApartamentoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['numero']
    search_fields = ['numero', 'torre']
    
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all().order_by('?')
    serializer_class = PessoaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'tipo']

class HidrometroViewSet(viewsets.ModelViewSet):
    queryset =  Hidrometro.objects.all().order_by('?')
    serializer_class = HidrometroSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['apartamento']
    search_fields = ['codigo', 'apartamento']

class LeituraViewSet(viewsets.ModelViewSet):
    queryset = Leitura.objects.all().order_by('?')
    serializer_class = LeituraSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['hidrometro']
    search_fields = ['hidrometro']
    

