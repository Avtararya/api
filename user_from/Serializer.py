
from rest_framework import serializers
from .models import Bodypart , Symptom

class BodypartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodypart
        fields = ['bodypart']

class SymsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Symptom
            fields = ['symptomname']










































 