from rest_framework import serializers
from gascontrolproject.models import Condominio, Torres

class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = ['nome', 'local']
        
class TorresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torres
        fields = ['nome']