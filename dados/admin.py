from django.contrib import admin
from dados.models import WW2


class ListarWW2(admin.ModelAdmin):
    list_display = ['pais', 'mortes_militares', 'mortes_civis', 'mortes_totais', 'populacao_inicial', 'percentage_of_population_mortes_totais', 'percentage_of_military_deaths', 'percentage_of_civilian_deaths']

admin.site.register(WW2, ListarWW2)