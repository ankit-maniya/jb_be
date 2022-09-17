class Fields:
    @staticmethod
    def partyListingField(instance):
        return {
            'id': instance.id,
            'p_name': instance.p_name,
            'p_mobile': instance.p_mobile,
        }

    @staticmethod
    def userListingField(instance):
        return {
            'id': instance.id,
            'u_name': instance.u_name,
            'u_email': instance.u_email,
        }
