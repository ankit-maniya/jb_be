from rest_framework import serializers
from .models import Partys


class PartyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partys
        fields = '__all__'
        read_only_fields = ['id']
