from rest_framework import serializers
from .models import CustomUser


class CustomeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone', 'otp', 'is_varified','password']

    def create(self, validated_data):
        user = CustomUser(
                        phone=validated_data['phone'],
                        )
        user.set_password(validated_data['password'])
        user.save()
        # send_otp_to_phone(validated_data['phone'])
        return user

class varifyAccountSerializer(serializers.Serializer):
    phone = serializers.CharField()
    otp = serializers.CharField()