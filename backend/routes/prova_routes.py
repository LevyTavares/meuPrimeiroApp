"""
Rotas para gerenciar provas (upload de imagens e processamento)
"""

from fastapi import APIRouter, UploadFile, File, Form
from typing import List
import json
import os
from datetime import datetime
from schemas import ProvaResponse

router = APIRouter()

PROVAS_FILE = "data/provas.json"

def ensure_data_dir():
    """Garantir que o diretório de dados existe"""
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("data/uploads"):
        os.makedirs("data/uploads")
    if not os.path.exists(PROVAS_FILE):
        with open(PROVAS_FILE, "w") as f:
            json.dump({"provas": [], "id_counter": 1}, f)

def load_provas():
    """Carregar provas do arquivo"""
    ensure_data_dir()
    with open(PROVAS_FILE, "r") as f:
        return json.load(f)

def save_provas(data):
    """Salvar provas no arquivo"""
    ensure_data_dir()
    with open(PROVAS_FILE, "w") as f:
        json.dump(data, f, indent=2)

@router.post("/", response_model=ProvaResponse)
async def submeter_prova(
    gabarito_id: int = Form(...),
    nome_aluno: str = Form(...),
    matricula_aluno: str = Form(...),
    turma_aluno: str = Form(...),
    imagem: UploadFile = File(...)
):
    """
    Submeter uma prova para correção
    
    - **gabarito_id**: ID do gabarito
    - **nome_aluno**: Nome do aluno
    - **matricula_aluno**: Matrícula do aluno
    - **turma_aluno**: Turma do aluno
    - **imagem**: Arquivo de imagem da prova
    """
    ensure_data_dir()
    
    # Salvar imagem
    filename = f"data/uploads/prova_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    with open(filename, "wb") as f:
        content = await imagem.read()
        f.write(content)
    
    data = load_provas()
    nova_prova = {
        "id": data["id_counter"],
        "gabarito_id": gabarito_id,
        "nome_aluno": nome_aluno,
        "matricula_aluno": matricula_aluno,
        "turma_aluno": turma_aluno,
        "imagem_url": filename,
        "respostas_detectadas": None,  # Será preenchido por OCR
        "criado_em": datetime.now().isoformat()
    }
    
    data["provas"].append(nova_prova)
    data["id_counter"] += 1
    save_provas(data)
    
    return nova_prova

@router.get("/", response_model=List[ProvaResponse])
async def listar_provas():
    """Listar todas as provas"""
    data = load_provas()
    return data["provas"]

@router.get("/{prova_id}", response_model=ProvaResponse)
async def obter_prova(prova_id: int):
    """Obter uma prova específica"""
    data = load_provas()
    prova = next(
        (p for p in data["provas"] if p["id"] == prova_id),
        None
    )
    if not prova:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Prova não encontrada")
    return prova

@router.delete("/{prova_id}")
async def deletar_prova(prova_id: int):
    """Deletar uma prova"""
    data = load_provas()
    prova_index = next(
        (i for i, p in enumerate(data["provas"]) if p["id"] == prova_id),
        None
    )
    if prova_index is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Prova não encontrada")
    
    # Deletar arquivo de imagem
    prova = data["provas"][prova_index]
    if os.path.exists(prova["imagem_url"]):
        os.remove(prova["imagem_url"])
    
    data["provas"].pop(prova_index)
    save_provas(data)
    
    return {"message": f"Prova {prova_id} deletada com sucesso"}
