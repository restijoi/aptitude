from rest_framework import serializers

from users.serializers import UserRegistrationSerializer
from .models import Stream

class StreamSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer(read_only=True)
    key = serializers.CharField(read_only =True)
    is_active = serializers.BooleanField(initial=True)
    ended_at = serializers.DateTimeField(read_only = False, allow_null=True)

    class Meta:
        model = Stream
        fields = ('user', 'is_active', 'key', 'started_at','ended_at')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(StreamSerializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):
        # create only 1 streaming
        if (self.Meta.model.objects.filter(user=self.request.user, is_active=True).exists()):
            raise serializers.ValidationError('Stream is already active')

        validated_data.update({'user':self.request.user})
        stream = super(StreamSerializer, self).create(validated_data)

        return stream
    
    def update(self, instance, data):
        instance.is_active = data.get('is_active') 
        instance.ended_at = data.get('ended_at')
        instance.save()
        return instance