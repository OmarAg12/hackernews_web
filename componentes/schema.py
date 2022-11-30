import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType

from .models import Componente


class ComponenteType(DjangoObjectType):
    class Meta:
        model = Componente


class Query(graphene.ObjectType):
    componentes = graphene.List(ComponenteType)

    def resolve_componentes(self, info, **kwargs):
        return Componente.objects.all()
# ...code
#1
class CreateComponente(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    semestre = graphene.String()

    class Arguments:
        name= graphene.String()
        semestre= graphene.String()

    def mutate(self, info, name, semestre):
        

        componente = Componente(
            name=name,
            semestre=semestre,
            
        )
        componente.save()

        return CreateComponente(
            id=componente.id,
            name=componente.name,
            semestre=componente.semestre,
            
        )


#4
class Mutation(graphene.ObjectType):
    create_componente = CreateComponente.Field()