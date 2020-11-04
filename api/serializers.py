from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (
    Especies,
    Arvores,
    GrupoArvores,
    Colheita
    )



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'groups']



class EspeciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Especies
        fields = ['id', 'descricao']

    
class ArvoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arvores
        fields = ['id','especies', 'descricao', 'idade']


class GrupoArvoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GrupoArvores
        fields = ['id','nome', 'descricao', 'arvores']

    
class ColheitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colheita
        fields = ['informacoes', 'data_colheita', 'peso_bruto', 'arvore']