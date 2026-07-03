import pandas as pd

def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    print("⚙️ [Transform] Iniciando limpeza e transformação dos dados...")
    
    # 1. Remover colunas de identificação textual que confundem o modelo de Machine Learning
    colunas_para_remover = ["id_cliente", "nome"]
    df_transformado = df.drop(columns=colunas_para_remover, errors="ignore")
    
    # 2. Tratamento preventivo de valores nulos (se houverem)
    df_transformado = df_transformado.dropna()
    
    print("✅ [Transform] Dados limpos e prontos para modelagem.")
    return df_transformado

if __name__ == "__main__":
    # Teste rápido se rodar isolado
    from src.pipeline.extract import extrair_dados_brutos
    df_bruto = extrair_dados_brutos()
    transformar_dados(df_bruto)
