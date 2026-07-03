import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)
random.seed(42)

num_clientes = 1000
dados = []

for i in range(num_clientes):
    # Definindo o perfil do cliente
    tempo_casa_meses = random.randint(1, 60)
    reclamacoes_suporte = random.randint(0, 10)
    
    # Criando uma lógica real de Churn baseada em comportamento
    # Mais reclamações e menos tempo de casa = Maior chance de Churn
    score_risco = (reclamacoes_suporte * 0.15) - (tempo_casa_meses * 0.01) + np.random.normal(0, 0.2)
    churn = 1 if score_risco > 0.2 else 0

    dados.append({
        "id_cliente": f"CLI-{1000 + i}",
        "nome": fake.name(),
        "idade": random.randint(18, 70),
        "tempo_casa_meses": tempo_casa_meses,
        "mensalidade_brl": round(random.uniform(49.90, 299.90), 2),
        "reclamacoes_suporte": reclamacoes_suporte,
        "uso_plataforma_horas": random.randint(0, 150),
        "churn": churn
    })

df = pd.DataFrame(dados)
df.to_csv("dados_clientes_churn.csv", index=False)
print("✅ Arquivo 'dados_clientes_churn.csv' gerado com sucesso!")
