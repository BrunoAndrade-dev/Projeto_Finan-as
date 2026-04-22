from django.urls import path
from .views import AvaliacaoFinancasCorretores, AvaliacaoFinancasEstagiarios, AvaliacaoFinancasExatas, AvaliacaoFinancasUFMA, AvaliacaoProjetoExtns

urlpatterns = [
    path('projeto-extensao/', AvaliacaoProjetoExtns.as_view(), name = 'api-financasprojetoextns' ),
    path('financas-exatas/',AvaliacaoFinancasExatas.as_view(), name = 'api-financasexatas'),
    path('financasufma/', AvaliacaoFinancasUFMA.as_view(), name = 'api-financasufma'),
    path('financasestagiarios/', AvaliacaoFinancasEstagiarios.as_view(),name = 'api-financasestagiarios') , 
    path('financas-corretores/', AvaliacaoFinancasCorretores.as_view(), name = 'api-financascorretores'),
]