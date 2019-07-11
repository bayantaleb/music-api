'''from rest_framework import serializers
from music.models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('artist', 'albums', 'song')
'''


import graphene
from music.models import Album
from graphene_django.types import DjangoObjectType


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class Query(graphene.ObjectType):
    all_albums = graphene.List(AlbumType)

    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.all()
