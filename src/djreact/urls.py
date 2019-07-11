
from django.contrib import admin
from django.urls import path, include

from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    #path('music/', include('music.urls', namespace='music')),
    path('graphql/', GraphQLView.as_view(
    graphiql = True,
    schema = schema
    )),
    path('admin/', admin.site.urls),
    path('api/', include('music.api.urls'))
]
