from rest_framework import serializers

from party_api.models import Partys
from party_api.serializers import PartyModelSerializer

from user_api.models import DjangoUser
from user_api.serializers import DjangoUserSerializer

from .models import Loats


class LoatsSerializer(serializers.ModelSerializer):
    userid = DjangoUserSerializer(read_only=True)
    partyid = PartyModelSerializer(read_only=True)

    class Meta:
        model = Loats
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context.get('user')
        partyId = self.context.get('partyId')

        validated_data['partyid'] = Partys.objects.get(id=partyId)
        validated_data['userid'] = DjangoUser.objects.get(id=user.id)
        validated_data['isactive'] = True

        return Loats.objects.create(**validated_data)
