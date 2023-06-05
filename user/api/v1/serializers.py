
from user.models import Profile, User
from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'password', 'postal_code', 'city', 'home_address']


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['phone', 'password']
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)



    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'password']
    
