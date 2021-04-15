from django.urls import path
from .views import UserCreateAPIView, UserListAPIView, UserRetrieveUpdateDestroyAPIView, UserLoginObtainView

urlpatterns = [
    path('', UserListAPIView.as_view(), name="users"),
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='get_users'),
    path('signup/', UserCreateAPIView.as_view(), name="signup"),
    path('login/', UserLoginObtainView.as_view(), name="login"),

]
