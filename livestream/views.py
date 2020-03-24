from rest_framework import permissions, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, UpdateAPIView

from .models import Stream
from .serializers import StreamSerializer

class StreamStartView(CreateAPIView):
    authentication_classes = (TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StreamSerializer

    def create(self, request):
        serializer = self.get_serializer(
            data = request.data,
            request = request
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=201)
    
    
    
class StreamStopView(UpdateAPIView):
    authentication_classes = (TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated)
    serializer_class = StreamSerializer
    queryset = Stream.objects.all()

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.get_serializer().Meta.model.objects.get(user= request.user.id, **kwargs),
            data = request.data,
            request = request
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=201)


    