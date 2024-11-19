from django.shortcuts import render, redirect
from dados.models import WW2
from rest_framework.exceptions import ValidationError
from dados.serializers import GeralSerializer
from rest_framework import viewsets, generics

class GeralViewSet(viewsets.ModelViewSet):
    queryset = WW2.objects.all()
    http_method_names = ['get']
    serializer_class = GeralSerializer


class PaisesPorMortesTotais(generics.ListAPIView):
    serializer_class = GeralSerializer
    def get_queryset(self):
        if self.request.content_type == 'application/json':
            mt = self.request.data.get('mt', None)
            comparison = self.request.data.get('comparison', None)
        else:
            mt = int(self.request.GET.get('mt'))
            comparison = self.request.GET.get('comparison')
        
        if not mt or not comparison:
            raise ValidationError('Parametros pm e comparison são obrigatórios')
        
        if comparison == "gte":
            queryset = WW2.objects.filter(mortes_totais__gte=mt).order_by('pais')
            return queryset
        if comparison =="lte":
            queryset = WW2.objects.filter(percentage_of_population_mortes_totais__lte=mt).order_by('pais')
            return queryset
        else:
            raise ValidationError('Parametro comparison deve ser "gte" para maior que ou "lte" para menor que')


class PaisesPorPercentualMortesTotais(generics.ListAPIView):
    serializer_class = GeralSerializer
    def get_queryset(self):
        if self.request.content_type == 'application/json':
            pm = self.request.data.get('pm', None)
            comparison = self.request.data.get('comparison', None)
        else:
            pm = int(self.request.GET.get('pm'))
            comparison = self.request.GET.get('comparison')
        
        if not pm or not comparison:
            raise ValidationError('Parametros pm e comparison são obrigatórios')
        
        if comparison == "gte":
            queryset = WW2.objects.filter(percentage_of_population_mortes_totais__gte=pm).order_by('-percentage_of_population_mortes_totais')
            return queryset
        if comparison =="lte":
            queryset = WW2.objects.filter(percentage_of_population_mortes_totais__lte=pm).order_by('percentage_of_population_mortes_totais')
            return queryset
        else:
            raise ValidationError('Parametro comparison deve ser "gte" para maior que ou "lte" para menor que')

class PaisesPorPercentualMortesMilitares(generics.ListAPIView):
    serializer_class = GeralSerializer
    def get_queryset(self):
        if self.request.content_type == 'application/json':
            pm = self.request.data.get('pm', None)
            comparison = self.request.data.get('comparison', None)
        else:
            pm = int(self.request.GET.get('pm'))
            comparison = self.request.GET.get('comparison')

        if not pm or not comparison:
            raise ValidationError('Parametros pm e comparison são obrigatórios')
        
        if comparison == "gte":
            queryset = WW2.objects.filter(percentage_of_military_deaths__gte=pm).order_by('-percentage_of_military_deaths')
            return queryset
        if comparison =="lte":
            queryset = WW2.objects.filter(percentage_of_military_deaths__lte=pm).order_by('percentage_of_military_deaths')
            return queryset
        else:
            raise ValidationError('Parametro comparison deve ser "gte" para maior que ou "lte" para menor que')

class PaisesPorPercentualMortesCivis(generics.ListAPIView):
    serializer_class = GeralSerializer
    def get_queryset(self):
        if self.request.content_type == 'application/json':
            pm = self.request.data.get('pm', None)
            comparison = self.request.data.get('comparison', None)
        else:
            pm = int(self.request.GET.get('pm'))
            comparison = self.request.GET.get('comparison')

        if not pm or not comparison:
            raise ValidationError('Parametros pm e comparison são obrigatórios')
        
        if comparison == "gte":
            queryset = WW2.objects.filter(percentage_of_civilian_deaths__gte=pm).order_by('-percentage_of_civilian_deaths')
            return queryset
        if comparison =="lte":
            queryset = WW2.objects.filter(percentage_of_civilian_deaths__lte=pm).order_by('percentage_of_civilian_deaths')
            return queryset
        else:
            raise ValidationError('Parametro comparison deve ser "gte" para maior que ou "lte" para menor que')