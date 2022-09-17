from rest_framework import serializers
from rest_framework.exceptions import APIException, ValidationError

from user_api.models import DjangoUser

from .models import Partys


class PartyModelSerializer(serializers.ModelSerializer):
    # userid = serializers.HyperlinkedRelatedField(
    #     view_name='django_user-detail', read_only=True)

    class Meta:
        model = Partys
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context.get('user')

        validated_data['userid'] = DjangoUser.objects.get(id=user.id)
        validated_data['isactive'] = True

        return Partys.objects.create(**validated_data)

# def validate(self, attrs):
#     print('self.context :: ')
#     if (self.context):
#         user = self.context.get('user')
#         # p_name = attrs.get('p_name')

#         if user is None:
#             raise ValidationError
#         ({"msg1": "Your Token Is Expired!"})

#         attrs['userid'] = DjangoUser.objects.get(id=user.id)
#         attrs['isactive'] = True

    # if p_name is None or len(p_name) <= 0:
    #     raise ValidationError(
    #         {"msg1": ["p_name field is required!", "p_name field is not empty!"]})

    # return attrs

# def validate_p_name(self, p_name):
#     if p_name is None or len(p_name) <= 0:
#         raise ValidationError(
#             {"msg1": ["p_name field is required!", "p_name field is not empty!"]})
#     return p_name
