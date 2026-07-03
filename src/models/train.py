import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def treinar_modelo_churn():
    caminho_dados = "data/processed/dados_clientes_limpos.csv"
    
    if not os.path.exists(caminho_dados):
        raise FileNotFoundError(f"❌ Dados processados não encontrados em: {caminho_dados}")
        
    print("🤖 [Data Science] Carregando dados da camada PROCESSED para o treino...")
    df = pd.read_csv(caminho_dados)
    
    # 1. Separar Variáveis Explicativas (X) e a Variável Alvo (y)
    X = df.drop(columns=["churn"])
    y = df["churn"]
    
    # 2. Dividir em dados de Treino (80%) e Teste (20%)
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print(f"📊 Dados de Treino: {X_treino.shape[0]} amostras | Dados de Teste: {X_teste.shape[0]} amostras")
    
    # 3. Inicializar e Treinar o Modelo
    print("🏋️‍♂️ Treinando o modelo Random Forest...")
    modelo = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=6)
    modelo.fit(X_treino, y_treino)
    
    # 4. Avaliar o Modelo com os dados de Teste
    predicoes = modelo.predict(X_teste)
    print("\n📈 --- Relatório de Performance do Modelo ---")
    print(f"Acurácia Geral: {accuracy_score(y_teste, predicoes):.2%}")
    print(classification_report(y_teste, predicoes))
    print("-------------------------------------------\n")
    
    # 5. Salvar o Modelo Treinado na pasta correta para a API usar
    caminho_modelo = "data/gold/modelo_churn.pkl"
    os.makedirs(os.path.dirname(caminho_modelo), exist_ok=True)
    
    with open(caminho_modelo, "wb") as f:
        pickle.dump(modelo, f)
        
    print(f"🚀 [Data Science] Sucesso! Modelo exportado com sucesso para: {caminho_modelo}")

if __name__ == "__main__":
    treinar_modelo_churn()
