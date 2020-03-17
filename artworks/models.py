from django.db import models
from django.conf import settings

from users.utils import artwork_media_path

class ArtWork(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    is_free = models.BooleanField(default=True)
    price = models.DecimalField(blank=True, null=True,  max_digits=19, decimal_places=10)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class ArtWorkImage(models.Model):
    artwork = models.ForeignKey('ArtWork', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=artwork_media_path, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class ArtWorkTag(models.Model):
    artwork = models.ForeignKey('ArtWork', on_delete=models.CASCADE)
    tag = models.CharField(max_length=255, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
