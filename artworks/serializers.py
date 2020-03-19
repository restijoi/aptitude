from rest_framework import serializers

from artworks.models import ArtWork, ArtWorkTag, ArtWorkImage
from users.serializers import UserRegistrationSerializer

class ArtWorkTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWorkTag
        fields = '__all__'

class ArtWorkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWorkImage
        fields = ('image',)

class ArtWorkSerializer(serializers.ModelSerializer):
    owner = UserRegistrationSerializer(read_only=True)
    image = serializers.ImageField(max_length=None, use_url=True, 
                                    allow_empty_file=True, write_only=True, 
                                    required=False)
    class Meta:
        model = ArtWork
        fields = ('title', 'description', 'image', 'is_free', 'price', 'owner' )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        return super(ArtWorkSerializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):    
        image = (lambda: validated_data.get('image'), lambda: None)[not validated_data.get('image')]()

        artWorkInstance = self.Meta.model.objects.create(
            owner = self.user,
            title = validated_data.get('title'),
            description = validated_data.get('description'),
            is_free = validated_data.get('is_free'),
            price = validated_data.get('price'),
        )
        
        if image:
            artWorkImageSerializer = ArtWorkImage.objects.create(
                artwork=artWorkInstance,
                image=image
            )
            validated_data['image'] = artWorkImageSerializer
        return validated_data
