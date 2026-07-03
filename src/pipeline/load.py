import pandas as pd
import os

def carregar_dados_processados(df: pd.DataFrame):
    caminho_processed = "data/processed/dados_clientes_limpos.csv"
    
    # Garantir que a pasta existe
    os.makedirs(os.path.dirname(caminho_processed), exist_ok=True)
    
    print("📤 [Load] Salvando dados na camada PROCESSED...")
    df.to_csv(caminho_processed, index=False)
    print(f"🚀 [Load] Pipeline concluído! Dados salvos em: {caminho_processed}")

if __name__ == "__main__":
    from src.pipeline.extract import extrair_dados_brutos
    from src.pipeline.transform import transformar_dados
    
    df_bruto = extrair_dados_brutos()
    df_limpo = transformar_dados(df_bruto)
    carregar_dados_processados(df_limpo)
