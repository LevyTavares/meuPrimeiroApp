"""
Rotas para gerenciar gabaritos
"""

from fastapi import APIRouter, HTTPException
from typing import List
import json
import os
from datetime import datetime
from schemas import GabaritoCreate, GabaritoResponse
from utils_gabarito import generate_gabarito_png, create_gabaritos_directory

router = APIRouter()

# Arquivo para persistência (simulando banco de dados)
GABARITOS_FILE = "data/gabaritos.json"

def ensure_data_dir():
    """Garantir que o diretório de dados existe"""
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(GABARITOS_FILE):
        with open(GABARITOS_FILE, "w") as f:
            json.dump({"gabaritos": [], "id_counter": 1}, f)

def load_gabaritos():
    """Carregar gabaritos do arquivo"""
    ensure_data_dir()
    with open(GABARITOS_FILE, "r") as f:
        return json.load(f)

def save_gabaritos(data):
    """Salvar gabaritos no arquivo"""
    ensure_data_dir()
    with open(GABARITOS_FILE, "w") as f:
        json.dump(data, f, indent=2)

@router.post("/", response_model=GabaritoResponse)
async def criar_gabarito(gabarito: GabaritoCreate):
    """
    Criar um novo gabarito
    
    - **titulo**: Título da prova
    - **num_questoes**: Número de questões
    - **alternativas**: Lista de alternativas (ex: ["A", "B", "C", "D", "E"])
    - **respostas_corretas**: Gabarito (ex: ["A", "C", "B", "D", ...])
    """
    # Validar respostas ANTES de criar o gabarito
    if len(gabarito.respostas_corretas) != gabarito.num_questoes:
        raise HTTPException(
            status_code=400,
            detail=f"Número de respostas ({len(gabarito.respostas_corretas)}) não corresponde ao número de questões ({gabarito.num_questoes})"
        )
    
    data = load_gabaritos()
    
    novo_gabarito = {
        "id": data["id_counter"],
        "titulo": gabarito.titulo,
        "num_questoes": gabarito.num_questoes,
        "alternativas": gabarito.alternativas,
        "respostas_corretas": gabarito.respostas_corretas,
        "descricao": gabarito.descricao,
        "criado_em": datetime.now().isoformat(),
        "atualizado_em": datetime.now().isoformat()
    }
    
    # Gerar gabarito em PNG
    try:
        gabarito_dir = create_gabaritos_directory()
        png_filename = os.path.join(
            gabarito_dir,
            f"gabarito_{novo_gabarito['id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )
        generate_gabarito_png(
            filename=png_filename,
            num_questions=gabarito.num_questoes,
            title=f"GABARITO - {gabarito.titulo}"
        )
        novo_gabarito["png_path"] = png_filename
    except Exception as e:
        print(f"Erro ao gerar PNG: {e}")
    
    data["gabaritos"].append(novo_gabarito)
    data["id_counter"] += 1
    save_gabaritos(data)
    
    return novo_gabarito

@router.get("/", response_model=List[GabaritoResponse])
async def listar_gabaritos():
    """Listar todos os gabaritos"""
    data = load_gabaritos()
    return data["gabaritos"]

@router.get("/{gabarito_id}", response_model=GabaritoResponse)
async def obter_gabarito(gabarito_id: int):
    """Obter um gabarito específico"""
    data = load_gabaritos()
    gabarito = next(
        (g for g in data["gabaritos"] if g["id"] == gabarito_id),
        None
    )
    if not gabarito:
        raise HTTPException(status_code=404, detail="Gabarito não encontrado")
    return gabarito

@router.put("/{gabarito_id}", response_model=GabaritoResponse)
async def atualizar_gabarito(gabarito_id: int, gabarito: GabaritoCreate):
    """Atualizar um gabarito"""
    data = load_gabaritos()
    gabarito_existente = next(
        (g for g in data["gabaritos"] if g["id"] == gabarito_id),
        None
    )
    if not gabarito_existente:
        raise HTTPException(status_code=404, detail="Gabarito não encontrado")
    
    gabarito_existente["titulo"] = gabarito.titulo
    gabarito_existente["num_questoes"] = gabarito.num_questoes
    gabarito_existente["alternativas"] = gabarito.alternativas
    gabarito_existente["respostas_corretas"] = gabarito.respostas_corretas
    gabarito_existente["descricao"] = gabarito.descricao
    gabarito_existente["atualizado_em"] = datetime.now().isoformat()
    
    save_gabaritos(data)
    return gabarito_existente

@router.delete("/{gabarito_id}")
async def deletar_gabarito(gabarito_id: int):
    """Deletar um gabarito"""
    data = load_gabaritos()
    gabarito_index = next(
        (i for i, g in enumerate(data["gabaritos"]) if g["id"] == gabarito_id),
        None
    )
    if gabarito_index is None:
        raise HTTPException(status_code=404, detail="Gabarito não encontrado")
    
    data["gabaritos"].pop(gabarito_index)
    save_gabaritos(data)
    
    return {"message": f"Gabarito {gabarito_id} deletado com sucesso"}
