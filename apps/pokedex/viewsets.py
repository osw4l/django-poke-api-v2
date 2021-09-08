from rest_framework import exceptions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PokemonSerializer
from .models import Pokemon
# Create your views here.


class PokemonViewSet(viewsets.GenericViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @action(detail=False, methods=['GET'], url_path='search/(?P<name>\w+)')
    def search(self, request, name):
        pokemons = Pokemon.objects.filter(name__icontains=name)

        if pokemons.count() == 0:
            raise exceptions.NotFound({"error": f'the pokemon {name} does not exist in the database'})

        serializer = self.serializer_class(pokemons.first())
        return Response(serializer.data)
