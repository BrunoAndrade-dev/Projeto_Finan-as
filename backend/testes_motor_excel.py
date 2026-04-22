import os 
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Pegando o motor 
from analisador.servicos.motor_excel import analise_descritiva
from pathlib import Path 

# CONFIGURAÇÃOES ESSENCIAIS DO TESTE MEU PARCEIRO
NOME_ARQUIVO = r"dataset_teste/AvaliacaoFinanceiraProjetoExtns.xlsx"

def executar_teste() :
    caminho = Path(NOME_ARQUIVO)

    if not caminho.exists(): 
        print(f"ERRO: O ARQUIVO '{NOME_ARQUIVO}' NÃO FOI ENCONTRADO. ")
        return
    print (f" --=-=- INICIANDO ANÁLSIE DO ARQUIVO REAL DA PROFESSORA...")

    resultado = analise_descritiva(caminho)

    if resultado["status"] == "sucesso" : 
        print ("\n SUCESSO!! O VizuData processou os dados corretamente.")
        print ("-" *50)

        print ("\n ESTATÍSTICAS NUMÉRICAS : ")
        print(json.dumps(resultado['analise']['numerica'], indent=2, ensure_ascii=False))
        
        # Mostra o resumo de texto (respostas do formulário)
        print("\n🗣️ TOP 5 RESPOSTAS (CATEGÓRICA):")

        print(json.dumps(resultado['analise']['categorica'], indent=2, ensure_ascii=False))
    else : 
        print (f"⚠️ Erro no Motor: {resultado['mensagem']}")

if __name__ == "__main__" : 
    executar_teste()

