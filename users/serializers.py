from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users.models import UserTag

from .utils import generate_handle

class UserTagSerializer(serializers.ModelSerializer):
    owner = None
    class Meta:
        model = UserTag
        fields = ('tag',)

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        return super(UserTagSerializer, self).__init__(*args, **kwargs)

    def create(self, data):
        data.update({'owner':self.owner})
        return super(UserTagSerializer, self).create(data)

class BaseUserSerializer(serializers.ModelSerializer):
    """ user serializer
    """
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
            'avatar',
            'tag'
        )

class UserRegistrationSerializer(BaseUserSerializer):
    tag = UserTagSerializer(write_only=True, many=True, allow_null=True, required=False)
    password = serializers.CharField(write_only=True, min_length=5, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True,min_length=5, style={'input_type': 'password'})
    avatar = serializers.ImageField(required=False, write_only=True)
    class Meta:
        model = get_user_model()
        fields = ('email' ,'first_name', 'last_name', 'password', 'confirm_password', 'tag', 'avatar')
    
    def validate(self, data):
        handle, domain = data.get('email').split('@')
        existing_handle = self.Meta.model.objects.filter(handle=handle)
        data.update({'handle': generate_handle(handle, existing_handle.count())})

        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("passwords don't match.")

        return data

    def create(self, validated_data):
        tag = validated_data.pop('tag', [])   
        user = get_user_model().objects.create_user(**validated_data)
        serializer = UserTagSerializer(data=tag, owner=user, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return validated_data

class AuthTokenSerializer(serializers.Serializer):
    user = None
    email = serializers.EmailField(
        required=True,
        write_only=True,
        label="Email"
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta(object):
        model = get_user_model()
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(AuthTokenSerializer, self).__init__(*args, **kwargs)

    def validate(self, data):
        """ validate email credentials
        """
        email, password = data.values()
        if not email or not password:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        self.user = authenticate(request=self.request, 
                                email=email, password=password)
        if not self.user:
            msg = _('Unable to log in with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        return data

    def get_token(self):
        """ get or generate a user token
        """
        if not self.user:
            msg = _('Unable to login with provided credentials.')
            raise serializers.ValidationError(msg, code="authorization")
        token, created = Token.objects.get_or_create(user=self.user)
        if created:
            token.delete()
            token = Token.objects.create(user=self.user)
        return (token)


class UserSerializer(BaseUserSerializer):
    """ user serializer
    """
    tag = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'avatar',
            'tag'
        )

    def get_tag(self, instance):
        return UserTagSerializer(
            UserTagSerializer.Meta.model.objects.filter(owner=instance),
            many=True
        ).data

