from rest_framework import serializers

from party_api.models import Partys
from party_api.serializers import PartyModelSerializer

from user_api.models import DjangoUser
from user_api.serializers import DjangoUserSerializer

from .models import Cuttingtypes


class CuttingTypesSerializer(serializers.ModelSerializer):
    userid = DjangoUserSerializer(read_only=True)
    partyid = PartyModelSerializer(read_only=True)

    #  Warning : django_user is a route name which defined in user_api app in urls, which is also same as url name
    # userid = serializers.HyperlinkedRelatedField(
    #     view_name="django_user-detail",
    #     read_only=True
    # )

    # partyid = serializers.HyperlinkedRelatedField(
    #     view_name="party_view-detail",
    #     read_only=True
    # )

    class Meta:
        model = Cuttingtypes
        fields = '__all__'
        read_only_fields = ['c_id']

    def create(self, validated_data):
        user = self.context.get('user')
        partyId = self.context.get('partyId')

        validated_data['partyid'] = Partys.objects.get(id=partyId)
        validated_data['userid'] = DjangoUser.objects.get(id=user.id)
        validated_data['isactive'] = True

        return Cuttingtypes.objects.create(**validated_data)
