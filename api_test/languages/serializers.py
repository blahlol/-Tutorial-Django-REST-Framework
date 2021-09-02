from rest_framework import serializers
from .models import Language,Paradigm

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Language
        fields=('id','name','paradigm')

class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paradigm
        fields=('id','name')