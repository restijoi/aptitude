from rest_framework import serializers

from artworks.models import ArtWork, ArtWorkTag, ArtWorkImage
from users.serializers import UserRegistrationSerializer

from users.utils import modify_image_input
class ArtWorkTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWorkTag
        fields = '__all__'

class ArtWorkImageSerializer(serializers.ModelSerializer):
    artwork = None
    class Meta:
        model = ArtWorkImage
        fields = ('image','is_featured',)
    
    def __init__(self, *args, **kwargs):
        self.artwork = kwargs.pop('artwork', None)
        return super(ArtWorkImageSerializer, self).__init__(*args, **kwargs)
    
    def create(self, data):
        data.update({'artwork':self.artwork})
        return super(ArtWorkImageSerializer, self).create(data)

class ArtWorkSerializer(serializers.ModelSerializer):
    owner = UserRegistrationSerializer(read_only=True)
    image = ArtWorkImageSerializer(write_only=False, required=False, many=True,source='artworkimage_set' )
    featured_image = ArtWorkImageSerializer(write_only=True,required=False, many=False)
    class Meta:
        model = ArtWork
        fields = ('title', 'description', 'featured_image', 'image', 'is_free', 'price', 'owner' )
        depth = 1

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(ArtWorkSerializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):
        images = dict((self.request.FILES).lists()).get('image', None)
        featured_image = dict((self.request.FILES).lists()).get('featured_image', None)
        images = modify_image_input(images, False)
        if featured_image:
            images.append(dict([('image', featured_image.pop()), ('is_featured', True)])) 

        art_work_instance = self.Meta.model.objects.create(owner=self.request.user, **validated_data)
        serializer = ArtWorkImageSerializer(data=images, artwork=art_work_instance, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return art_work_instance
