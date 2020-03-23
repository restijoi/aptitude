from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import response, permissions, authentication, generics
from .serializers import ArtWorkSerializer
from .models import ArtWork

class ArtWorkViewSets(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ArtWorkSerializer
    queryset = ArtWork.objects.all()

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data,
            request=request
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=201)

        