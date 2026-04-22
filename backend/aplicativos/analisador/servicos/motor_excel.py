import pandas as pd 
import numpy as np 

def analise_descritiva (arquivo_enviado) : 
    """
    Aqui não preciso explicar muito, mas ja explicando...essa função recebe o arquivo(excel) que ja passou por toda validação no views.py.  o método describe() do pandas gera uma análise descritiva completa do DataFrame, incluindo contagem, média, desvio padrão, valores mínimos , máximos, quartis e adicionei de quebra a mediana e a moda (ISSO COM O SELECT_DTYPES PARA NUMEROS), para análise categórica de textos fiz  o select_dtypes para incluir "object" e "category". Além disso, também contei os valores nulos em cada coluna para fornecer uma visão mais completa dos dados. O resultado é organizado em um dicionário que inclui informações gerais sobre o DataFrame e as estatísticas descritivas, pronto para ser enviado de volta ao front-end.
    """
    try :
        extensao = str(arquivo_enviado).lower()

        if extensao.endswith('.csv') : 
            df = pd.read_csv(arquivo_enviado, encoding='utf-8-sig', sep=',')
        else : 
            df = pd.read_excel(arquivo_enviado)
            

        if df.empty : 
            return {"status" : "erro" , 
            "mensagem" : "O arquivo Excel está vazio. Por favor, envie um arquivo com dados."}
        
        # Análise para colunas numéricas
        df_numerico = df.select_dtypes(include=[np.number])
        stats_numericos = []

        if not df_numerico.empty :
            descricao_numerica = df_numerico.describe().transpose()
            descricao_numerica["mediana"] = df_numerico.median()
            descricao_numerica["moda"] = df_numerico.mode().iloc[0]
            stats_numericos = descricao_numerica.reset_index().rename(columns={"index" : "coluna"}).to_dict(orient="records")

        # Análise para colunas categóricas
        df_texto = df.select_dtypes(include=["object", "category"])
        stats_categoricos = []

        if not df_texto.empty :
            for coluna in df_texto : 
                top_valores = df_texto[coluna].value_counts().head(5).to_dict()
                stats_categoricos.append({
                    "coluna" : coluna,
                    "total_unicos" : df_texto[coluna].nunique(),
                    "mais_frequentes" : top_valores, 
                    "valores_nulos" : int(df_texto[coluna].isnull().sum())
                })
        return {
            "status" : "sucesso",
            "metadados" : {
                "linhas" : len(df),
                "colunas" : len(df) , 
            }, 
            "analise" : {
                "numerica" : stats_numericos,
                "categorica" : stats_categoricos
            }
        }

    except Exception as e : 
        return {"status" : "erro" , "mensagem" : str(e)}

def analise_de_distribuicao(arquivo_enviado) : 
    """
    Função responsável por fazer a análise de distribuição, ou seja, aqui vamos poder analisar desigualdades e padrões das bases de dados ---
    
    """    
        