import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="ChurnGuard AI - Dashboard", layout="wide", page_icon="📊")

st.title("📊 ChurnGuard AI - Painel Estratégico de Retenção")
st.markdown("Acompanhamento financeiro de clientes em risco e métricas de Lifetime Value (LTV).")

# 1. Carregar os dados processados pelo pipeline
caminho_dados = "data/processed/dados_clientes_limpos.csv"

if not os.path.exists(caminho_dados):
    st.error(f"❌ Base de dados não encontrada em {caminho_dados}. Execute o pipeline primeiro.")
else:
    df = pd.read_csv(caminho_dados)
    
    # 2. Cálculos de Métricas de Negócio (KPIs)
    total_clientes = len(df)
    clientes_churn = df[df['churn'] == 1]
    taxa_churn = len(clientes_churn) / total_clientes
    
    mrr_total = df['mensalidade_brl'].sum()
    mrr_em_risco = clientes_churn['mensalidade_brl'].sum()
    
    # 3. Exibição dos Blocos de KPIs no topo do painel
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Total de Clientes", f"{total_clientes:,}")
    kpi2.metric("Taxa de Churn", f"{taxa_churn:.2%}")
    kpi3.metric("Faturamento Mensal (MRR)", f"R$ {mrr_total:,.2f}")
    kpi4.metric("Receita em Risco (Crítica)", f"R$ {mrr_em_risco:,.2f}", delta=f"-{mrr_em_risco/mrr_total:.1%}", delta_color="inverse")
    
    st.markdown("---")
    
    # 4. Construção dos Gráficos com Plotly
    graf1, graf2 = st.columns(2)
    
    with graf1:
        st.subheader("⚠️ Reclamações no Suporte vs. Cancelamento")
        fig_suporte = px.histogram(df, x="reclamacoes_suporte", color="churn", 
                                   barmode="group", labels={"churn": "Cancelou?"},
                                   color_discrete_sequence=["#2ecc71", "#e74c3c"])
        st.plotly_chart(fig_suporte, use_container_width=True)
        
    with graf2:
        st.subheader("⏳ Tempo de Casa (Meses) do Cliente")
        fig_tempo = px.box(df, x="churn", y="tempo_casa_meses", color="churn",
                           labels={"churn": "Cancelou?"},
                           color_discrete_sequence=["#2ecc71", "#e74c3c"])
        st.plotly_chart(fig_tempo, use_container_width=True)

    # 5. Tabela Dinâmica de Clientes Críticos
    st.markdown("---")
    st.subheader("🚨 Lista de Ação Imediata (Clientes com Churn Confirmado pelo Modelo)")
    clientes_criticos = df[df['churn'] == 1].sort_values(by="mensalidade_brl", ascending=False)
    st.dataframe(clientes_criticos, use_container_width=True)
