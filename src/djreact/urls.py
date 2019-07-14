
from django.contrib import admin
from django.urls import path, include

from graphene_django.views import GraphQLView
from .schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    #path('music/', include('music.urls', namespace='music')),



    path('graphql/',csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('admin/', admin.site.urls),
    path('api/', include('music.api.urls'))
]
