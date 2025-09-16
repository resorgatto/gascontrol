from rest_framework import serializers
from gascontrolproject.models import Condominio, Torres, Apartamento, Pessoa, Hidrometro, Leitura

class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = ['id', 'nome', 'local']
        
class TorresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torres
        fields = ['id', 'numero', 'identificacao', 'condominio']
        
class ApartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartamento
        fields = ['id', 'numero', 'torre']

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
        
class HidrometroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hidrometro
        fields = '__all__'

class LeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitura
        fields = '__all__'
        
class LeituraDetailSerializer(serializers.ModelSerializer):
    hidrometro = HidrometroSerializer(read_only=True)
    apartamento = serializers.CharField(source='hidrometro.apartamento.numero', read_only=True)
    torre = serializers.CharField(source='hidrometro.apartamento.torre.identificacao', read_only=True)
    condominio = serializers.CharField(source='hidrometro.apartamento.torre.condominio.nome', read_only=True)
    
    class Meta:
        model = Leitura
        fields = '__all__'
