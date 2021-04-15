from .models import UserProfile
from .serializer import UserProfileSerializer
from .permissions import UpdateOwnProfile


from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserCreateAPIView(generics.CreateAPIView):
    """
    create api for user create
    """
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    queryset = UserProfile.objects.all()


class UserListAPIView(generics.ListAPIView):
    """
    list api for users
    """
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    queryset = UserProfile.objects.all()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
      Retrieve Update Destroy users API
    """
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    queryset = UserProfile.objects.all()


class UserLoginObtainView(ObtainAuthToken):
    """
    handle create user auth tokens
    """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
