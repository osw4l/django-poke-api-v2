from django.urls import path, include
from rest_framework import routers
from . import viewsets, views


app_name = 'pokedex'
router = routers.DefaultRouter()
router.register(r'pokedex', viewsets.PokemonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.SearchView.as_view()),
]
