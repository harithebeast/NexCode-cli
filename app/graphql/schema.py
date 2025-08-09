import strawberry
from app.graphql.queries.user_queries import Query
from app.graphql.mutations.user_mutations import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
