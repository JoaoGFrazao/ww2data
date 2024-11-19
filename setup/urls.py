from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dados.views import GeralViewSet, PaisesPorMortesTotais, PaisesPorPercentualMortesTotais, PaisesPorPercentualMortesCivis, PaisesPorPercentualMortesMilitares

router = routers.DefaultRouter()
router.register('geral', GeralViewSet, basename='Geral')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('paises-mortes-totais', PaisesPorMortesTotais.as_view(), name='paises_por_mortes_totais'),
    path('percentual-mortes-totais', PaisesPorPercentualMortesTotais.as_view(), name='paises_por_percentual'),
    path('percentual-mortes-militares', PaisesPorPercentualMortesMilitares.as_view(), name='paises_por_percentual_militares'),
    path('percentual-mortes-civis', PaisesPorPercentualMortesCivis.as_view(), name='paises_por_percentual_civis'),
]
