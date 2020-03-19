from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users.models import UserTag

from .utils import generateHandle

class UserTagSerializer(serializers.ModelSerializer):
    owner = None
    class Meta:
        model = UserTag
        fields = ('tag',)

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        return super(UserTagSerializer, self).__init__(*args, **kwargs)

    def create(self, data):
        self.Meta.model.objects.create(owner=self.owner ,**data)
        return data


class UserRegistrationSerializer(serializers.ModelSerializer):
    tag = UserTagSerializer(write_only=True, many=True, allow_null=True, required=False)

    class Meta:
        model = get_user_model()
        fields = ('email' ,'first_name', 'last_name', 'password', 'tag')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5,'style':{'input_type': 'password'}}}
    
    def validate(self, data):
        handle = data.get('email').split('@')[0]
        existingHandle = self.Meta.model.objects.filter(handle=handle)
        generatedHandle = generateHandle(handle, existingHandle.count())
        data['handle']  = generatedHandle

        return data

    def create(self, validated_data):
        tag = validated_data.pop('tag', None)
        user = get_user_model().objects.create_user(**validated_data)
        serializer = UserTagSerializer(data=tag, owner=user , many=True)
        if (serializer.is_valid()):
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
        super(AuthTokenSerializer, self).__init__(*args, **kwargs)

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
