from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'Choice', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def create_user_serializer(self, data):
        """serialize new user """
        user = UserProfile(email=data['email'],
                           username=data['username'],
                           Choice=data['Choice'],
                           password=data['password'])

        user.set_password('password')
        user.save(self._db)
        return user
