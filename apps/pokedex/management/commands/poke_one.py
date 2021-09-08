from django.core.management.base import BaseCommand
from apps.utils.colors import red, green, cyan
from apps.pokedex.helpers import PokeApiV2


class Command(BaseCommand):
    help = 'Displays current time'

    def add_arguments(self, parser):
        parser.add_argument('pokemon', nargs='+', type=str, help='Pokemon ID')

    def handle(self, *args, **kwargs):
        pokemon_name = kwargs.get('pokemon')[0]
        print('looking for {}'.format(
            green(pokemon_name)
        ))

        api = PokeApiV2()
        api.search(pokemon=pokemon_name)


