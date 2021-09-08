from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import Pokemon, Evolution
# Register your models here.


class EvolutionInline(admin.StackedInline):
    model = Evolution
    extra = 0


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'weight',
        'height'
    ]
    search_fields = [
        'name'
    ]
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    inlines = (
        EvolutionInline,
    )
    
