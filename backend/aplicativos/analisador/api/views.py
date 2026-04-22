import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from analisador.servicos.motor_excel import analise_descritiva

# Aqui resolvi criar uma Classe base para reaproveitar a lógica de leitura do servidor

class BaseView (APIView) : 
    # Essa bomba aqui só vai ser definida depois
    arquivo_nome = None

    def get (self, request) : 
        if not self.arquivo_nome : 
            return Response({'erro': 'Arquivo não encontrado.'}, status=500)
        
        # Navegando até onde os datasets de teste estão sendo guardados.
        caminho = os.path.join(settings.BASE_DIR, 'dataset_teste',self.arquivo_nome)

        if not os.path.exists(caminho):
            return Response ({'erro': f'Arquivo {self.arquivo_nome} não encontrado.'}, status=404)
        
        resultado = analise_descritiva(caminho)
        return Response(resultado)
    
class AvaliacaoProjetoExtns(BaseView) : 
    arquivo_nome = 'AvaliacaoFinanceiraProjetoExtns.xlsx'

class AvaliacaoFinancasUFMA(BaseView) : 
    arquivo_nome = 'AvaliacaoFinanceiraUFMA.xlsx'

class AvaliacaoFinancasExatas(BaseView):
    arquivo_nome = 'AvaliacaoFinanceiraExatas.xlsx'

class AvaliacaoFinancasEstagiarios(BaseView) :
    arquivo_nome = 'AvaliacaoFinanceiraEstagiarios.xlsx'

class AvaliacaoFinancasCorretores(BaseView):
    arquivo_nome = 'AvaliacaoFinanceiraCorretores.xlsx'
    