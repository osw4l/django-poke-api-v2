from django.core.management.base import BaseCommand
from apps.pokedex.helpers import PokeApi
from apps.pokedex.models import Pokemon, Evolution
from apps.utils.colors import red, green, cyan


class Command(BaseCommand):
    help = 'Get All Pokemons from poke api v2'

    def handle(self, *args, **kwargs):
        print('Getting Data From - {}-{}-{}'.format(
            green(msg='Poke'),
            red(msg='Api'),
            cyan(msg='V2'),
        ))

        print('...')

        api = PokeApi()
        api.get_pokemons()
        print(red('Error -> the process was interrupted because the remote server refused the connection'))

