

from .models import Profile
from rooms.serializers import RoomInfoSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    dev_rooms = RoomInfoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'dev_rooms',)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class ProfileSerializer(serializers.ModelSerializer):
    dev_rooms = RoomInfoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Profile
        fields = ('number', 'user', 'mylinks', 'dev_rooms')
        extra_kwargs = {'url': {'lookup_url': 'user'}}