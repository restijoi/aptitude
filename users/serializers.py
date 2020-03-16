import datetime
from itertools import islice

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import UserTag

class UserRegistrationSerializers(serializers.ModelSerializer):
    tag = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id','email' ,'first_name', 'last_name', 'description', 'username', 'password','tag')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5,'style':{'input_type': 'password'}}}

    def validate_username(self, value):
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError("Username Already Exist.")
        return value
    
    def create(self, validated_data):
        email, f_name, l_name, description, username, password, tags = validated_data.values()
        user = get_user_model().objects.create_user(email, username, password, first_name = f_name, last_name = l_name, description=description)
        objs = (UserTag(tag=tag, owner=user) for tag in tags.split(','))
        while True: #batch create
            batch = list(islice(objs, 10))
            if not batch:
                break
            UserTag.objects.bulk_create(batch, 10)

        return user

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

    token = serializers.CharField(
        allow_blank=True,
        read_only=True
    )

    class Meta(object):
        model = get_user_model()
        fields = ('username', 'password','token')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AuthTokenSerializer, self).__init__(*args, **kwargs)

    def validate(self, data):
        """ validate email credentials
        """
        username, password = data.values()
        
        if not username or not password:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        self.user = authenticate(request=self.request,
                                 username=username, password=password)

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
        
        token = RefreshToken.for_user(self.user)

        return 'Bearer '+str(token)