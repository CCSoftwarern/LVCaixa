from rest_framework import serializers
from appcaixa import models
from django.contrib.auth.models import User

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.empresa
        fields = '__all__'

class tipo_movimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tipo_movimento
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.clientes
        fields = '__all__'
        
class MovimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.movimento
        fields = '__all__'

class folhapgtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.folhapgto
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
      