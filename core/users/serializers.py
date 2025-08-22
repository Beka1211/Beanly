from rest_framework import serializers
from .models import MyUser

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password','phone_number','is_active','is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return MyUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number'],
            is_active=validated_data['is_active'],
            is_staff=validated_data['is_staff']
        )
