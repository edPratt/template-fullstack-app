from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from nucleus.models import Person


User = get_user_model()


class UserType(DjangoObjectType):
  class Meta:
    model = User

class PersonType(DjangoObjectType):
  class Meta:
    model = Person
