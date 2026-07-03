# 🛡️ ChurnGuard AI: Previsão de Churn e Proteção de Receita Baseada em LTV

Este projeto implementa uma solução de ponta a ponta para combater a maior dor das empresas atuais: o cancelamento de clientes (Churn). Ele une **Engenharia de Dados**, **Ciência de Dados** e **Desenvolvimento de Software** para prever o comportamento de risco de clientes e calcular o impacto financeiro (MRR em risco) em tempo real.

---

## 🎯 A Dor do Negócio
Adquirir um novo cliente custa até 7 vezes mais caro do que manter um atual. Empresas que não antecipam o Churn perdem faturamento de forma silenciosa. O **ChurnGuard AI** atua preventivamente, gerando alertas automáticos para o time de Sucesso do Cliente (Customer Success) agir antes que o cancelamento aconteça.

---

## 🏗️ Arquitetura do Projeto

O projeto foi dividido de forma modular seguindo as melhores práticas do mercado de tecnologia:

1. **Engenharia de Dados (Pipeline ETL):** Ingestão automática, limpeza e transformação de dados brutos (`data/raw`) para dados processados prontos para modelagem (`data/processed`).
2. **Ciência de Dados (Machine Learning):** Algoritmo *Random Forest Classifier* treinado com **94.00% de acurácia geral** para predição probabilística de cancelamento.
3. **Desenvolvimento (API em FastAPI):** Endpoint de produção que recebe dados cadastrais e comportamentais e responde em milissegundos com o score de risco do cliente.
4. **Análise de Dados (Dashboard Streamlit):** Painel executivo interativo focado em métricas financeiras (LTV, MRR Total e Receita Crítica em Risco).

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem Principal:** Python 3.12
* **Engenharia / Manipulação:** Pandas, NumPy
* **Machine Learning / IA:** Scikit-Learn
* **Framework Web & API:** FastAPI, Uvicorn, Pydantic
* **Visualização de Dados:** Streamlit, Plotly
* **DevOps / Infraestrutura:** Docker, Python-Virtualenv

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o repositório e preparar o ambiente
```bash
git clone https://github.com
cd churn_guand_ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Executar a esteira de dados e o treino do modelo
```bash
# Executa a geração de dados e pipeline ETL
python notebooks/gerar_dados.py
mv dados_clientes_churn.csv data/raw/
PYTHONPATH=. python src/pipeline/load.py

# Treina a inteligência artificial
PYTHONPATH=. python src/models/train.py
```

### 3. Iniciar a API de Produção
```bash
PYTHONPATH=. uvicorn src.api.main:app --reload
```
Acesse a documentação interativa (Swagger UI) em: `http://127.0.0`

### 4. Iniciar o Dashboard de Análise de Dados
```bash
streamlit run dashboard/app_streamlit.py
```
Acesse o painel executivo em: `http://localhost:8501`

---

## 🐳 Executando via Docker Container
Se preferir rodar a aplicação encapsulada sem instalar dependências locais:
```bash
docker build -t churn-guard-ai .
docker run -p 8000:8000 churn-guard-ai
```

---
✉️ **Desenvolvido por [Seu Nome]** - Conecte-se comigo no [LinkedIn](seu-link-aqui).
