from django.urls import path, include
from django.conf.urls import url

from .views import StreamStartView, StreamStopView
from rest_framework import routers

router = routers.DefaultRouter()

app_name = 'stream'

urlpatterns = [
    path('', include(router.urls)),
    path("start-stream/", StreamStartView.as_view(), name="start-stream"),
    url(r'^stop-stream/(?P<key>[0-9A-Za-z_\-]+)/$', StreamStopView.as_view(), name="stop-stream"),
]
