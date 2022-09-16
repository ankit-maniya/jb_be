from rest_framework import serializers

from party_api.models import Partys
from party_api.serializers import PartyModelSerializer
from user_api.serializers import DjangoUserSerializer
from .models import Cuttingtypes


class CuttingTypesSerializer(serializers.ModelSerializer):
    # userid = DjangoUserSerializer()
    partyid = PartyModelSerializer()

    #  Warning : django_user is a route name which defined in user_api app in urls, which is also same as url name
    userid = serializers.HyperlinkedRelatedField(
        view_name="django_user-detail",
        read_only=True
    )

    # partyid = serializers.HyperlinkedRelatedField(
    #     view_name="party_view-detail",
    #     read_only=True
    # )

    class Meta:
        model = Cuttingtypes
        # fields = ['id', 'u_name', 'u_billingname', 'u_mobile']
        fields = '__all__'
        read_only_fields = ['id']
