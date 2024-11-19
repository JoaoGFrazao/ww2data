import os
import django
import csv
import pandas as pd
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()
from dados.models import WW2
from decimal import Decimal

db_final = pd.read_csv('ww2_data - ww2_deaths.csv')
db_suplente = pd.read_csv('ww2_dataset.csv')
db_suplente_filtrada = db_suplente[['Country', 'Total population as of 1/1/1939']].copy()
db_suplente_filtrada.rename(columns={'Total population as of 1/1/1939': 'initial_population'}, inplace=True)

db_final_merged = pd.merge(db_final, db_suplente_filtrada, on='Country', how='left')
db_final_merged['initial_population'] = db_final_merged['initial_population'].str.replace(',', '', regex=False).astype(float)
db_final_merged.to_csv('ww2_final.csv', index=False)
db_merged = pd.merge(db_final, db_suplente_filtrada)

def parse_float(value):
    try:
        return float(value.replace(',', '').strip()) if value.strip() else None
    except ValueError:
        return None  # Retorna None se a conversão falhar

with open('ww2_final.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Carregar os dados do CSV, convertendo os campos numéricos para float
        pais = row['Country']
        mortes_militares = parse_float(row['Military_Deaths'])
        mortes_civis = parse_float(row['Civilian_deaths'])
        mortes_totais = parse_float(row['Total_deaths'])
        populacao_inicial = parse_float(row['initial_population'])

        # Criar a instância do modelo com os dados convertidos
        WW2.objects.create(
            pais=pais,
            mortes_militares=mortes_militares,
            mortes_civis=mortes_civis,
            mortes_totais=mortes_totais,
            populacao_inicial=populacao_inicial
        )

table = WW2.objects.all()

for pais in table:
    #Percentual de mortes civis de acordo com o total de mortes
    if pais.mortes_civis == 0 or pais.mortes_totais == 0:
        pais.percentage_of_civilian_deaths = None
    else:
        percentual_cd = round(Decimal(pais.mortes_civis / pais.mortes_totais), 5)
        percentual_cd = 100 * percentual_cd
        pais.percentage_of_civilian_deaths = percentual_cd

    #Percentual de mortes militares de acordo com o total de mortes
    if pais.mortes_militares == 0 or pais.mortes_totais == 0:
        pais.percentage_of_military_deaths = None
    else:
        percentual_md = round(Decimal(pais.mortes_militares / pais.mortes_totais), 5)
        percentual_md = 100 * percentual_md
        pais.percentage_of_military_deaths = percentual_md

    #Percentual de mortes totais de acordo com a população inicial
    if pais.mortes_totais == 0 or pais.populacao_inicial == 0:
        pais.percentage_of_population_mortes_totais = None
    elif pais.mortes_totais is None or pais.populacao_inicial is None:
        pais.percentage_of_population_mortes_totais = None
    else:
        percentual_td = round(Decimal(pais.mortes_totais / pais.populacao_inicial), 5)
        percentual_td = 100 * percentual_td
        pais.percentage_of_population_mortes_totais = percentual_td
    
    #Salvar alterações
    pais.save()