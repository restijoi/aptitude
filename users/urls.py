from django.urls import path, include
from users.views import UserRegistrationView, UserLoginView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('register', UserRegistrationView, basename='register',)

app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', UserLoginView.as_view(), name="login"),
]
