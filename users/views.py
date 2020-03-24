from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions, response, status, authentication
from rest_framework.viewsets import ViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.settings import api_settings
from rest_framework.response import Response

from users.serializers import UserRegistrationSerializer, AuthTokenSerializer, UserSerializer

class UserRegistrationView(CreateAPIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegistrationSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

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

class AuthUser(ViewSet):
    """ auth user endpoint
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=200)


