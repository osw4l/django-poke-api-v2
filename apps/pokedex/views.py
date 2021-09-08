from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import ProcessFormView
from apps.pokedex.helpers import PokeApiV2
from apps.utils.shortcuts import get_object_or_none
from .models import Pokemon

poke_api = PokeApiV2()


class SearchView(TemplateView,
                 ProcessFormView):
    template_name = 'search.html'
    template_context = {
        'result': None,
        'pokemon': None,
        'fetched': False
    }
    pokemon = None

    def post(self, request, *args, **kwargs):
        self.pokemon = request.POST.get('pokemon')
        pokemon = self.get_pokemon()
        if not pokemon:
            result = self.fetch_pokemon()
            if result:
                self.template_context = {
                    'result': True,
                    'pokemon': result,
                    'fetched': True
                }
            else:
                self.template_context['result'] = False
        else:
            self.template_context['result'] = True
            self.template_context['pokemon'] = pokemon
        self.template_context['search'] = self.pokemon
        return render(request, self.template_name, context=self.template_context)

    def get_pokemon(self):
        return get_object_or_none(Pokemon, name__icontains=self.pokemon)

    def fetch_pokemon(self):
        last = poke_api.search(self.pokemon)
        return last if last and last.name.lower() == self.pokemon.lower() else None
