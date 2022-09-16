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

    def validate(self, attrs):
        user = self.context.get('user')
        p_name = attrs.get('p_name')

        if user is None:
            raise ValidationError({'msg1': "Your Token Is Expired!"})

        attrs['userid'] = DjangoUser.objects.get(id=user.id)
        attrs['isactive'] = True

        if p_name is None or len(p_name) <= 0:
            raise ValidationError(
                {'msg1': "p_name field is required!", 'msg2': "p_name field is not empty!"})

        return attrs
