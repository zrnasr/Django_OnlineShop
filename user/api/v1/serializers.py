
from user.models import Profile, User
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'password', 'postal_code', 'city', 'home_address']


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['phone', 'password']


class RegisterSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    class Meta:
        model = User
        fields = ['phone', 'password']

