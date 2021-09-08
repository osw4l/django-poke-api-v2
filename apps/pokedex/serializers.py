from rest_framework import serializers
from .models import Pokemon, Evolution


class EvolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evolution
        fields = (
            'id',
            'name',
            'evolution_type'
        )


class PokemonSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='pokemon_id')
    evolutions = EvolutionSerializer(read_only=True, many=True)

    class Meta:
        model = Pokemon
        fields = (
            'id',
            'name',
            'height',
            'weight',
            'base_stats',
            'evolutions',
        )

