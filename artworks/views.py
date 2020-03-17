from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import response, mixins, permissions, authentication, generics
from .serializers import ArtWorkSerializer
from .models import ArtWork

class ArtWorkViewSets(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.AllowAny,)
    # parser_classes = (MultiPartParser, FormParser)
    serializer_class = ArtWorkSerializer
    queryset = ArtWork.objects.all()

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data,
            user=request.user
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(serializer.data, status=201)

    # def post(self, request):
    #     try:
    #         images = dict((request.data).lists())['image.image']
    #         serializer = self.serializer_class(
    #             data=request.data,
    #         )
    #         serializer.is_valid(raise_exception=True)
    #         return response.Response(serializer.data, status=200)
    #     except KeyError:
    #         print( KeyError)
    #         raise Http404('Request has no resource file attached')

        