from rest_framework import serializers
from .user_model import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        # fields = ['id', 'u_name', 'u_billingname', 'u_mobile']
        fields = '__all__'
        read_only_fields = ['id']
