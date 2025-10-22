"""
TEstify Backend - API REST para o sistema de correção de provas
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn
import os
from dotenv import load_dotenv

# Importar rotas
from routes import gabarito_routes, prova_routes, resultado_routes

load_dotenv()

# Inicializar FastAPI
app = FastAPI(
    title="TEstify API",
    description="Backend do sistema TEstify de correção de provas",
    version="1.0.0"
)

# Configurar CORS para aceitar requisições do frontend mobile
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(gabarito_routes.router, prefix="/api/gabaritos", tags=["Gabaritos"])
app.include_router(prova_routes.router, prefix="/api/provas", tags=["Provas"])
app.include_router(resultado_routes.router, prefix="/api/resultados", tags=["Resultados"])

# Health check
@app.get("/health")
async def health():
    """Verificar status da API"""
    return {
        "status": "ok",
        "message": "TEstify Backend está funcionando"
    }

@app.get("/")
async def root():
    """Rota raiz com informações da API"""
    return {
        "nome": "TEstify API",
        "versão": "1.0.0",
        "descrição": "Backend do sistema de correção de provas",
        "endpoints": {
            "gabaritos": "/api/gabaritos",
            "provas": "/api/provas",
            "resultados": "/api/resultados",
            "docs": "/docs",
            "health": "/health"
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=os.getenv("DEBUG", "false").lower() == "true"
    )
