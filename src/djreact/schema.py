import graphene
from music.api.schema import Query as albums_query

class Query(albums_query):
    pass

schema = graphene.Schema(query = Query)
