class Fields:
    @staticmethod
    def PartyListingField(instance):
        return {
            'id': instance.id,
            'p_name': instance.p_name,
            'p_mobile': instance.p_mobile,
        }

    @staticmethod
    def UserListingField(instance):
        return {
            'id': instance.id,
            'u_name': instance.u_name,
            'u_email': instance.u_email,
        }
