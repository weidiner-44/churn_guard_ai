import os
import pandas as pd

def extrair_dados_brutos():
    caminho_raw = "data/raw/dados_clientes_churn.csv"
    
    if not os.path.exists(caminho_raw):
        raise FileNotFoundError(f"❌ Arquivo bruto não encontrado em: {caminho_raw}. Certifique-se de rodar o gerador de dados antes.")
        
    print("📥 [Extract] Carregando dados brutos da camada RAW...")
    df = pd.read_csv(caminho_raw)
    print(f"✅ [Extract] Sucesso! {df.shape[0]} registros carregados.")
    return df

if __name__ == "__main__":
    extrair_dados_brutos()
