from rest_framework.generics import ListAPIView, RetrieveAPIView
from music.models import Album

from .serializers import AlbumSerializer

class AlbumListAPIView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailAPIView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
