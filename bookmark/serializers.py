from rest_framework import serializers
from .models import source

class sourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = source
        fields = '__all__'
