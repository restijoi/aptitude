from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

from functools import partial
from django.utils.crypto import get_random_string

class Stream(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="stream", on_delete=models.CASCADE)
    key = models.CharField(max_length=20, default=partial(get_random_string, 20), unique=True)

    is_active = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    ended_at = models.DateTimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.user.handle

    @property
    def is_live(self):
        return self.started_at is not None

    @property
    def hls_url(self):
        return reverse("hls-url", args=(self.user.handle,))