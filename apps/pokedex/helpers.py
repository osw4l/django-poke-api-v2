import requests
import abc

from apps.pokedex.constants import PREEVOLUTION, EVOLUTION
from apps.pokedex.models import Pokemon, Evolution
from apps.utils.colors import red, green, cyan, orange, purple, blue
from apps.utils.shortcuts import get_object_or_none


class Api(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    http_client = requests
    pokemons = []

    def send_request(self, url):
        response = self.http_client.get(url)
        return response.json()

    @abc.abstractmethod
    def send_paginated_request(self, url):
        pass

    def process_insert(self):
        pokemons = []
        evolutions = []
        print(cyan('Fetch process done !'))
        last = None

        print(green('Creating Pokemons'))
        for poke in self.pokemons:
            if not get_object_or_none(Pokemon, pokemon_id=poke.get('id')):
                pokemon = Pokemon.objects.create(
                    pokemon_id=poke.get('id'),
                    name=poke.get('name'),
                    weight=poke.get('weight'),
                    height=poke.get('height'),
                    base_stats=poke.get('stats')
                )
                pokemons.append(pokemon)

                for ev in poke.get('evolutions'):
                    evolution = Evolution(
                        pokemon_id=pokemon.id,
                        name=ev.get('name'),
                        evolution_type=ev.get('evolution_type')
                    )
                    evolutions.append(evolution)
            else:
                print(red('Error: {} already exist in the database'.format(
                    cyan(poke.get('name'))
                )))

        if len(evolutions) > 0:
            print(cyan('Creating Evolutions'))
            Evolution.objects.bulk_create(evolutions)

            print('Total Pokemons: {}'.format(
                cyan(len(self.pokemons))
            ))

            print(green('Database full, process done!'))
            last = pokemons.pop()
            pokemons.clear()
            evolutions.clear()
        self.pokemons.clear()
        return last


class PokeApi(Api):
    start_url = 'https://pokeapi.co/api/v2/pokemon/'
    pokemon_evolutions = []

    def get_pokemons(self):
        print('Sending first request to : {}'.format(
            cyan(self.start_url)
        ))

        self.send_paginated_request(url=self.start_url)
        self.process_insert()
        self.pokemon_evolutions.clear()

    def send_paginated_request(self, url):
        response = super().send_request(url=url)

        for result in response.get('results'):
            poke = self.retrieve_pokemon(url=result.get('url'))
            self.pokemons.append(poke)

        if response.get('next'):
            print('====== >>>>>>> {} - {} <<<<<<< ======'.format(
                purple('Navigating for the next page'),
                red(response.get('next'))
            ))
            # self.send_paginated_request(url=response.get('next'))

    def process_evolution_chain(self, chain):
        species = chain.get('species')
        print(purple(species))
        if species:
            self.pokemon_evolutions.append({
                'name': species.get('name'),
                'evolution_type': PREEVOLUTION if chain.get('is_baby') else EVOLUTION
            })
            print(blue(self.pokemon_evolutions))
            if len(chain.get('evolves_to')) > 0:
                next_pokemon = chain.get('evolves_to')[0]
                self.process_evolution_chain(next_pokemon)

        return self.pokemon_evolutions

    def get_evolution_chain(self, url, pokemon_id):
        self.pokemon_evolutions.clear()

        print('{} #{} in {}'.format(
            orange('Getting specie detail for pokemon'),
            green(pokemon_id),
            cyan(url)
        ))

        evolution_chain_url = super().send_request(
            url=url
        ).get('evolution_chain').get('url')

        print('{} #{} in {}'.format(
            orange('Getting evolution chain for pokemon'),
            green(pokemon_id),
            cyan(evolution_chain_url)
        ))
        evolution_chain_response = super().send_request(url=evolution_chain_url).get('chain')

        return self.process_evolution_chain(chain=evolution_chain_response)

    def retrieve_pokemon(self, url):
        print('Making single request for : {}'.format(
            cyan(url)
        ))
        response = super().send_request(url=url)

        stats_response = response.get('stats')
        stats = []
        for stat in stats_response[:6]:
            stats.append({
                'name': stat.get('stat').get('name'),
                'base_stat': stat.get('base_stat'),
                'effort': stat.get('effort'),
            })

        pokemon_id = response.get('id')
        pokemon_specie_detail_url = response.get('species').get('url')

        evolutions = self.get_evolution_chain(url=pokemon_specie_detail_url, pokemon_id=pokemon_id)

        return {
            'id': pokemon_id,
            'name': response.get('name'),
            'height': response.get('height'),
            'weight': response.get('weight'),
            'stats': stats,
            'evolutions': evolutions
        }


class PokeApiV2(PokeApi):
    pokemon = None

    def search(self, pokemon):
        result = None
        self.pokemon = pokemon.replace(' ', '').lower()
        print(f'search {self.pokemon}')
        self.send_paginated_request(url=self.start_url)

        try:
            result = self.process_insert()
        except:
            print('{}'.format(
                red('Error, {} doesnt exists inside of PokeApiV2'.format(cyan(self.pokemon)))
            ))

        return result

    def send_paginated_request(self, url):
        response = super().send_request(url=url)
        for result in response.get('results'):
            if result.get('name').lower() == self.pokemon:
                poke = super().retrieve_pokemon(url=result.get('url'))
                self.pokemons.append(poke)
                return

        if response.get('next'):
            print('====== >>>>>>> {} - {} <<<<<<< ======'.format(
                purple('Navigating for the next page'),
                red(response.get('next'))
            ))
            self.send_paginated_request(url=response.get('next'))
