from django.db import models

class WW2 (models.Model):
    pais = models.CharField(null=False, blank=False, max_length=100)
    mortes_militares = models.IntegerField(null=False, blank=True)
    mortes_civis = models.IntegerField(null=False, blank=True)
    mortes_totais = models.IntegerField(null=False, blank=True)
    populacao_inicial =  models.IntegerField(null=True, blank=True)
    percentage_of_population_mortes_totais = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=5)
    percentage_of_military_deaths = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=5)
    percentage_of_civilian_deaths = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=5)
