from pydantic import BaseModel, Field

class ClienteInput(BaseModel):
    id_cliente: str = Field(..., example="CLI-1001")
    nome: str = Field(..., example="João Silva")
    idade: int = Field(..., gt=0, example=30)
    tempo_casa_meses: int = Field(..., ge=0, example=12)
    mensalidade_brl: float = Field(..., gt=0.0, example=99.90)
    reclamacoes_suporte: int = Field(..., ge=0, example=2)
    uso_plataforma_horas: int = Field(..., ge=0, example=45)
