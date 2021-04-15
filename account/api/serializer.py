from rest_framework import serializers
from django.contrib.auth.models import User

User_Type = [
    ("Doctor", "Doctor"),
    ("patient", "patient"),
]


class UserProfile(serializers.ModelSerializer):
    user_choice = serializers.models.CharField(choices=User_Type)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_choice', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'

                          }
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['user_type'],
            validated_data['password'])

        return user
