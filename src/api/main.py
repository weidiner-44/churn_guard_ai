from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd
import os
from src.api.schemas import ClienteInput

app = FastAPI(
    title="ChurnGuard AI API",
    description="API de produção para previsão de Churn de clientes em tempo real.",
    version="1.0.0"
)

MODEL_PATH = "data/gold/modelo_churn.pkl"

def carregar_modelo():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Modelo não encontrado em {MODEL_PATH}. Treine o modelo primeiro.")
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

try:
    modelo_churn = carregar_modelo()
    print("✅ [API] Modelo preditivo carregado com sucesso em memória!")
except Exception as e:
    print(f"❌ [API] Erro ao carregar o modelo: {str(e)}")
    modelo_churn = None

@app.get("/")
def home():
    status_modelo = "Pronto" if modelo_churn else "Modelo Não Carregado"
    return {
        "status": "Online",
        "projeto": "ChurnGuard AI",
        "status_modelo": status_modelo
    }

@app.post("/v1/clientes/prever")
def prever_churn_cliente(cliente: ClienteInput):
    if not modelo_churn:
        raise HTTPException(status_code=500, detail="Modelo preditivo não disponível no servidor.")
    
    try:
        dados_cliente = pd.DataFrame([{
            "idade": cliente.idade,
            "tempo_casa_meses": cliente.tempo_casa_meses,
            "mensalidade_brl": cliente.mensalidade_brl,
            "reclamacoes_suporte": cliente.reclamacoes_suporte,
            "uso_plataforma_horas": cliente.uso_plataforma_horas
        }])
        
        predicao = int(modelo_churn.predict(dados_cliente))
        probabilidade = float(modelo_churn.predict_proba(dados_cliente)[:, 1])
        
        if probabilidade > 0.7:
            risco = "ALTO"
        elif probabilidade > 0.35:
            risco = "MÉDIO"
        else:
            risco = "BAIXO"
            
        return {
            "id_cliente": cliente.id_cliente,
            "nome_cliente": cliente.nome,
            "previsao_churn": predicao,
            "probabilidade_churn": round(probabilidade * 100, 2),
            "classificacao_risco": risco,
            "mensagem_estrategica": "⚠️ Acionar time de retenção imediatamente!" if risco == "ALTO" else "✅ Cliente saudável."
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro no processamento da previsão: {str(e)}")

import os
from src.api.schemas import ClienteInput

app = FastAPI(
    title="ChurnGuard AI API",
    description="API de produção para previsão de Churn de clientes em tempo real.",
    version="1.0.0"
)

MODEL_PATH = "data/gold/modelo_churn.pkl"

def carregar_modelo():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Modelo não encontrado em {MODEL_PATH}. Treine o modelo primeiro.")
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

try:
    modelo_churn = carregar_modelo()
    print("✅ [API] Modelo preditivo carregado com sucesso em memória!")
except Exception as e:
    print(f"❌ [API] Erro ao carregar o modelo: {str(e)}")
    modelo_churn = None

@app.get("/")
def home():
    status_modelo = "Pronto" if modelo_churn else "Modelo Não Carregado"
    return {
        "status": "Online",
        "projeto": "ChurnGuard AI",
        "status_modelo": status_modelo
    }

@app.post("/v1/clientes/prever")
def prever_churn_cliente(cliente: ClienteInput):
    if not modelo_churn:
        raise HTTPException(status_code=500, detail="Modelo preditivo não disponível no servidor.")
    
    try:
        dados_cliente = pd.DataFrame([{
            "idade": cliente.idade,
            "tempo_casa_meses": cliente.tempo_casa_meses,
            "mensalidade_brl": cliente.mensalidade_brl,
            "reclamacoes_suporte": cliente.reclamacoes_suporte,
            "uso_plataforma_horas": cliente.uso_plataforma_horas
        }])
        
        predicao = int(modelo_churn.predict(dados_cliente))
        probabilidade = float(modelo_churn.predict_proba(dados_cliente)[:, 1][0])
        
        if probabilidade > 0.7:
            risco = "ALTO"
        elif probabilidade > 0.35:
            risco = "MÉDIO"
        else:
            risco = "BAIXO"
            
        return {
            "id_cliente": cliente.id_cliente,
            "nome_cliente": cliente.nome,
            "previsao_churn": predicao,
            "probabilidade_churn": round(probabilidade * 100, 2),
            "classificacao_risco": risco,
            "mensagem_estrategica": "⚠️ Acionar time de retenção imediatamente!" if risco == "ALTO" else "✅ Cliente saudável."
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro no processamento da previsão: {str(e)}")
