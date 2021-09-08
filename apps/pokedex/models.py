from django.db import models
from .constants import EVOLUTION, EVOLUTION_TYPES


class Pokemon(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    pokemon_id = models.PositiveIntegerField(unique=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    base_stats = models.JSONField()

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemons'

    def __str__(self):
        return self.name


class Evolution(models.Model):
    pokemon = models.ForeignKey(
        'pokedex.Pokemon',
        on_delete=models.CASCADE,
        related_name='evolutions'
    )
    name = models.CharField(
        max_length=100
    )
    evolution_type = models.CharField(
        max_length=15,
        choices=EVOLUTION_TYPES,
        default=EVOLUTION
    )

    class Meta:
        verbose_name = 'Evolution'
        verbose_name_plural = 'Evolutions'


