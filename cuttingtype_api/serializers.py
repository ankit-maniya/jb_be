from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from party_api.models import Partys
from party_api.serializers import PartyModelSerializer

from user_api.models import DjangoUser
from user_api.serializers import DjangoUserSerializer
from utils.field_listing import Fields

from .models import Cuttingtypes


class PartyListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return Fields.PartyListingField(instance)


class UserListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return Fields.UserListingField(instance)


class CuttingTypesSerializer(serializers.ModelSerializer):
    # userid = DjangoUserSerializer(read_only=True)
    # partyid = PartyModelSerializer(read_only=True)

    partyid = PartyListingField(read_only=True)
    userid = UserListingField(read_only=True)

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

        try:
            validated_data['partyid'] = Partys.objects.get(id=partyId)
            validated_data['userid'] = DjangoUser.objects.get(id=user.id)
        except Exception as e:
            raise ValidationError({"db_error": e})

        validated_data['isactive'] = True

        return Cuttingtypes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        partyId = self.context.get('partyId')

        if partyId != 0:
            instance.partyid = Partys.objects.get(id=partyId)

        instance.save()
        return instance
