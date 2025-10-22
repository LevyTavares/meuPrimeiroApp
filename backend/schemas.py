"""
Schemas (Pydantic models) para validação de dados
"""

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# ===== GABARITO =====
class GabaritoCreate(BaseModel):
    """Schema para criar um novo gabarito"""
    titulo: str
    num_questoes: int
    alternativas: List[str]  # ["A", "B", "C", "D", "E"]
    respostas_corretas: List[str]  # ["A", "C", "B", "D", "E", ...]
    descricao: Optional[str] = None

class GabaritoUpdate(BaseModel):
    """Schema para atualizar gabarito"""
    titulo: Optional[str] = None
    respostas_corretas: Optional[List[str]] = None
    descricao: Optional[str] = None

class GabaritoResponse(BaseModel):
    """Schema de resposta para gabarito"""
    id: int
    titulo: str
    num_questoes: int
    alternativas: List[str]
    respostas_corretas: List[str]
    descricao: Optional[str]
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True

# ===== PROVA =====
class ProvaCreate(BaseModel):
    """Schema para submeter uma prova para correção"""
    gabarito_id: int
    nome_aluno: str
    matricula_aluno: str
    turma_aluno: str
    imagem_url: Optional[str] = None  # URL da imagem ou base64

class ProvaResponse(BaseModel):
    """Schema de resposta para prova"""
    id: int
    gabarito_id: int
    nome_aluno: str
    matricula_aluno: str
    turma_aluno: str
    imagem_url: Optional[str]
    respostas_detectadas: Optional[List[str]]
    criado_em: datetime

    class Config:
        from_attributes = True

# ===== RESULTADO =====
class ResultadoCreate(BaseModel):
    """Schema de criação de resultado (JSON body)"""
    prova_id: int
    gabarito_id: int
    respostas_aluno: List[str]

class ResultadoResponse(BaseModel):
    """Schema de resposta para resultado da correção"""
    id: int
    prova_id: int
    gabarito_id: int
    nome_aluno: str
    matricula_aluno: str
    turma_aluno: str
    respostas_aluno: List[str]
    respostas_corretas: List[str]
    acertos: int
    erros: int
    percentual_acerto: float
    nota: float
    criado_em: datetime

    class Config:
        from_attributes = True

# ===== ESTATISTICAS =====
class EstatisticasResponse(BaseModel):
    """Schema para estatísticas de um gabarito"""
    gabarito_id: int
    total_provas_corrigidas: int
    media_acertos: float
    media_erros: float
    media_percentual: float
    questao_mais_errada: int
    questao_mais_acertada: int
