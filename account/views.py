from .models import UserProfile
from rest_framework import generics
from .serializer import UserProfileSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    create api for user create
    """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserListAPIView(generics.ListAPIView):
    """
    list api for users
    """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
      Retrieve Update Destroy users API
    """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
