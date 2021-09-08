import sys
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Pokemon, Evolution


class SearchTestCase(APITestCase):
    pokemon = {}

    def setUp(self):
        stats = [
            {
                "name": "hp",
                "base_stat": 35,
                "effort": 0
            },
            {
                "name": "attack",
                "base_stat": 55,
                "effort": 0
            },
            {
                "name": "defense",
                "base_stat": 40,
                "effort": 0
            },
            {
                "name": "special-attack",
                "base_stat": 50,
                "effort": 0
            },
            {
                "name": "special-defense",
                "base_stat": 50,
                "effort": 0
            },
            {
                "name": "speed",
                "base_stat": 90,
                "effort": 2
            }
        ]

        pokemon = Pokemon.objects.create(
            name='pikachu',
            pokemon_id=25,
            height=4,
            weight=60,
            base_stats=stats
        )

        evolutions = [
            {
                "name": "pichu",
                "evolution_type": "Preevolution"
            },
            {
                "name": "pikachu",
                "evolution_type": "Evolution"
            },
            {
                "name": "raichu",
                "evolution_type": "Evolution"
            }
        ]

        for ev in evolutions:
            Evolution.objects.create(
                pokemon=pokemon,
                name=ev.get('name'),
                evolution_type=ev.get('evolution_type')
            )

        self.pokemon = {
            "id": 25,
            "name": "pikachu",
            "height": 4,
            "weight": 60,
            "base_stats": [
                {
                    "name": "hp",
                    "base_stat": 35,
                    "effort": 0
                },
                {
                    "name": "attack",
                    "base_stat": 55,
                    "effort": 0
                },
                {
                    "name": "defense",
                    "base_stat": 40,
                    "effort": 0
                },
                {
                    "name": "special-attack",
                    "base_stat": 50,
                    "effort": 0
                },
                {
                    "name": "special-defense",
                    "base_stat": 50,
                    "effort": 0
                },
                {
                    "name": "speed",
                    "base_stat": 90,
                    "effort": 2
                }
            ],
            "evolutions": [
                {
                    "name": "pichu",
                    "evolution_type": "Preevolution"
                },
                {
                    "name": "pikachu",
                    "evolution_type": "Evolution"
                },
                {
                    "name": "raichu",
                    "evolution_type": "Evolution"
                }
            ]
        }

    def test_search_ok(self):
        response = self.client.get('/api/pokedex/search/pikachu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_get_pokemon_ok(self):
        response = self.client.get('/api/pokedex/search/pikachu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_get_pokemon_data_ok(self):
        response = self.client.get('/api/pokedex/search/pikachu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.pokemon)

    def test_search_fail(self):
        response = self.client.get('/api/pokedex/search/pikachu2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_search_fail_404_message(self):
        response = self.client.get('/api/pokedex/search/pikachu2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {'error': 'the pokemon pikachu2 does not exist in the database'})

