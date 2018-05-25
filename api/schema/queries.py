import graphene

from django.contrib.auth import get_user_model

from django.contrib.auth import get_user_model

from schema import types

User = get_user_model()

class UserQuery:
    all_users = graphene.List(types.UserType)
    self = graphene.Field(types.UserType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_self(self, info, **kwargs):
        if info.context.user.is_authenticated:
            return info.context.user
        return None


class AuthenticationQuery:
    is_authenticated = graphene.Field(graphene.Boolean)

    def resolve_is_authenticated(self, info, **kwargs):
        return info.context.user.is_authenticated


class Query(
            AuthenticationQuery,
            graphene.ObjectType):
    pass


