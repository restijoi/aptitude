from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions, response, status
from rest_framework.generics import CreateAPIView
from rest_framework.settings import api_settings

from users.serializers import UserRegistrationSerializer, AuthTokenSerializer

class UserRegistrationView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegistrationSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data
        )
        
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class UserLoginView(ObtainAuthToken):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = AuthTokenSerializer

    def post(self, request):
        """ accepts post data that contains user credentials
            and validates it. Returns a generated token.
        """
        serializer = self.serializer_class(
            data=request.data, 
            request=request
        )
        serializer.is_valid(raise_exception=True)
        return response.Response({
            'token': serializer.get_token().key,
            'user_id': serializer.user.id
        }, status=201)


