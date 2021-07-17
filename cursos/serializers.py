from rest_framework import serializers
from .models import Curso

#class CursoSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Curso
#        fields = ('id', 'nome', 'tipo', 'preço')

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'url', 'nome', 'tipo', 'preço')