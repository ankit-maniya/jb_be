from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from party_api.models import Partys
# from party_api.serializers import PartyModelSerializer

from user_api.models import DjangoUser
# from user_api.serializers import DjangoUserSerializer

from utils.field_listing import Fields

from .models import Loats


class PartyListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return Fields.partyListingField(instance)


class UserListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return Fields.userListingField(instance)


class LoatsSerializer(serializers.ModelSerializer):
    # userid = DjangoUserSerializer(read_only=True)
    # partyid = PartyModelSerializer(read_only=True)

    # userid = serializers.PrimaryKeyRelatedField(read_only=True)
    # partyid = serializers.PrimaryKeyRelatedField(read_only=True)

    partyid = PartyListingField(read_only=True)
    userid = UserListingField(read_only=True)

    class Meta:
        model = Loats
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context.get('user')
        partyId = self.context.get('partyId')

        try:
            validated_data['partyid'] = Partys.objects.get(id=partyId)
            validated_data['userid'] = DjangoUser.objects.get(id=user.id)
        except Exception as e:
            raise ValidationError({"db_error": e})

        validated_data['isactive'] = True

        # return Loats.objects.create(**validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        partyId = self.context.get('partyId')

        if partyId != 0:
            try:
                instance.partyid = Partys.objects.get(id=partyId)
            except Exception as e:
                raise ValidationError({"db_error": e})

        return super().update(instance, validated_data)
