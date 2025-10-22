"""
Rotas para resultados das correções
"""

from fastapi import APIRouter, HTTPException
from typing import List
import json
import os
from datetime import datetime
from schemas import ResultadoResponse, EstatisticasResponse, ResultadoCreate

router = APIRouter()

RESULTADOS_FILE = "data/resultados.json"
GABARITOS_FILE = "data/gabaritos.json"
PROVAS_FILE = "data/provas.json"

def ensure_data_dir():
    """Garantir que o diretório de dados existe"""
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(RESULTADOS_FILE):
        with open(RESULTADOS_FILE, "w") as f:
            json.dump({"resultados": [], "id_counter": 1}, f)

def load_resultados():
    """Carregar resultados do arquivo"""
    ensure_data_dir()
    with open(RESULTADOS_FILE, "r") as f:
        return json.load(f)

def load_gabaritos():
    """Carregar gabaritos"""
    with open(GABARITOS_FILE, "r") as f:
        return json.load(f)

def load_provas():
    """Carregar provas"""
    with open(PROVAS_FILE, "r") as f:
        return json.load(f)

def save_resultados(data):
    """Salvar resultados no arquivo"""
    ensure_data_dir()
    with open(RESULTADOS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def calcular_resultado(respostas_aluno: List[str], gabarito_id: int) -> dict:
    """
    Calcular o resultado da correção
    """
    gabaritos_data = load_gabaritos()
    gabarito = next(
        (g for g in gabaritos_data["gabaritos"] if g["id"] == gabarito_id),
        None
    )
    
    if not gabarito:
        raise HTTPException(status_code=404, detail="Gabarito não encontrado")
    
    respostas_corretas = gabarito["respostas_corretas"]
    
    acertos = sum(
        1 for a, c in zip(respostas_aluno, respostas_corretas) if a == c
    )
    erros = len(respostas_aluno) - acertos
    percentual = (acertos / len(respostas_aluno) * 100) if respostas_aluno else 0
    nota = (acertos / len(respostas_aluno) * 10) if respostas_aluno else 0
    
    return {
        "acertos": acertos,
        "erros": erros,
        "percentual_acerto": round(percentual, 2),
        "nota": round(nota, 2)
    }

@router.post("/", response_model=ResultadoResponse)
async def criar_resultado(payload: ResultadoCreate):
    """
    Criar um resultado de correção
    
    - **prova_id**: ID da prova
    - **gabarito_id**: ID do gabarito
    - **respostas_aluno**: Respostas do aluno detectadas ou inseridas
    """
    provas_data = load_provas()
    prova = next(
        (p for p in provas_data["provas"] if p["id"] == payload.prova_id),
        None
    )
    
    if not prova:
        raise HTTPException(status_code=404, detail="Prova não encontrada")
    
    # Calcular resultado
    calculo = calcular_resultado(payload.respostas_aluno, payload.gabarito_id)
    
    # Obter gabarito para pegar respostas corretas
    gabaritos_data = load_gabaritos()
    gabarito = next(
        (g for g in gabaritos_data["gabaritos"] if g["id"] == payload.gabarito_id),
        None
    )
    if not gabarito:
        raise HTTPException(status_code=404, detail="Gabarito não encontrado")
    
    data = load_resultados()
    novo_resultado = {
        "id": data["id_counter"],
        "prova_id": payload.prova_id,
        "gabarito_id": payload.gabarito_id,
        "nome_aluno": prova["nome_aluno"],
        "matricula_aluno": prova["matricula_aluno"],
        "turma_aluno": prova["turma_aluno"],
        "respostas_aluno": payload.respostas_aluno,
        "respostas_corretas": gabarito["respostas_corretas"],
        **calculo,
        "criado_em": datetime.now().isoformat()
    }
    
    data["resultados"].append(novo_resultado)
    data["id_counter"] += 1
    save_resultados(data)
    
    return novo_resultado

@router.get("/", response_model=List[ResultadoResponse])
async def listar_resultados():
    """Listar todos os resultados"""
    data = load_resultados()
    return data["resultados"]

@router.get("/{resultado_id}", response_model=ResultadoResponse)
async def obter_resultado(resultado_id: int):
    """Obter um resultado específico"""
    data = load_resultados()
    resultado = next(
        (r for r in data["resultados"] if r["id"] == resultado_id),
        None
    )
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado não encontrado")
    return resultado

@router.get("/gabarito/{gabarito_id}/estatisticas", response_model=EstatisticasResponse)
async def obter_estatisticas(gabarito_id: int):
    """
    Obter estatísticas de um gabarito
    (quais questões mais erraram, média de acertos, etc)
    """
    data = load_resultados()
    resultados_gabarito = [
        r for r in data["resultados"] if r["gabarito_id"] == gabarito_id
    ]
    
    if not resultados_gabarito:
        raise HTTPException(status_code=404, detail="Nenhum resultado encontrado para este gabarito")
    
    total = len(resultados_gabarito)
    media_acertos = sum(r["acertos"] for r in resultados_gabarito) / total
    media_erros = sum(r["erros"] for r in resultados_gabarito) / total
    media_percentual = sum(r["percentual_acerto"] for r in resultados_gabarito) / total
    
    # Encontrar questão mais errada
    erros_por_questao = {}
    gabaritos_data = load_gabaritos()
    gabarito = next(
        (g for g in gabaritos_data["gabaritos"] if g["id"] == gabarito_id),
        None
    )
    
    for resultado in resultados_gabarito:
        for i, (resposta, correta) in enumerate(zip(resultado["respostas_aluno"], resultado["respostas_corretas"])):
            if resposta != correta:
                erros_por_questao[i] = erros_por_questao.get(i, 0) + 1
    
    questao_mais_errada = max(erros_por_questao, key=erros_por_questao.get) if erros_por_questao else 0
    questao_mais_acertada = min(erros_por_questao, key=erros_por_questao.get) if erros_por_questao else 0
    
    return {
        "gabarito_id": gabarito_id,
        "total_provas_corrigidas": total,
        "media_acertos": round(media_acertos, 2),
        "media_erros": round(media_erros, 2),
        "media_percentual": round(media_percentual, 2),
        "questao_mais_errada": questao_mais_errada,
        "questao_mais_acertada": questao_mais_acertada
    }

@router.delete("/{resultado_id}")
async def deletar_resultado(resultado_id: int):
    """Deletar um resultado"""
    data = load_resultados()
    resultado_index = next(
        (i for i, r in enumerate(data["resultados"]) if r["id"] == resultado_id),
        None
    )
    if resultado_index is None:
        raise HTTPException(status_code=404, detail="Resultado não encontrado")
    
    data["resultados"].pop(resultado_index)
    save_resultados(data)
    
    return {"message": f"Resultado {resultado_id} deletado com sucesso"}
