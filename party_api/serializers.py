from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user_api.models import DjangoUser
from user_api.serializers import DjangoUserSerializer

from utils.field_listing import Fields

from .models import Partys


class UserListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return Fields.UserListingField(instance)


class PartyModelSerializer(serializers.ModelSerializer):
    userid = DjangoUserSerializer(read_only=True)
    userid = UserListingField(read_only=True)
    # userid = serializers.HyperlinkedRelatedField(
    #     view_name='django_user-detail', read_only=True)

    class Meta:
        model = Partys
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context.get('user')

        try:
            validated_data['userid'] = DjangoUser.objects.get(id=user.id)
        except Exception as e:
            raise ValidationError({"db_error": e})

        validated_data['isactive'] = True

        return Partys.objects.create(**validated_data)
