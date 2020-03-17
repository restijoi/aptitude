from django.urls import path, include
from .views import ArtWorkViewSets

from rest_framework import routers

router = routers.DefaultRouter()
# router.register('artwork', ArtWorkViewSets, basename='artwork',)

app_name = 'artworks'

urlpatterns = [
    path('', include(router.urls)),
    path('artwork/', ArtWorkViewSets.as_view(), name="artwork"),
]
