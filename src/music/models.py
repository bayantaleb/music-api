from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length = 100)
    albums = models.CharField(max_length = 100)
    song = models.CharField(max_length = 100)

    def __str__(self):
        return self.artist
