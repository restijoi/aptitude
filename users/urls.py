from django.urls import path, include
from users.views import UserRegistrationView, UserLoginView, AuthUser

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name="login"),
    path('auth/user/', AuthUser.as_view({'get': 'get' }), name="auth_user"),
]
