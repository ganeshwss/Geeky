from dataclasses import fields
from rest_framework import serializers
from .models import *

class TransformerSerializer(serializers.ModelSerializer):
    class Meta:
        fields=("__all__")
        model=Transformer
