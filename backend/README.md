# 🚀 TEstify Backend API

Backend para o sistema TEstify de correção de provas.

## 📦 Tecnologias

- **FastAPI** - Framework Web moderno
- **Uvicorn** - Servidor ASGI
- **Pillow** - Geração de gabaritos em PNG
- **OpenCV** - Processamento de imagens
- **Tesseract OCR** - Reconhecimento óptico de caracteres
- **Docker** - Containerização

## 🏗️ Estrutura

```
backend/
├── main.py              # Aplicação principal
├── schemas.py           # Modelos Pydantic
├── utils_gabarito.py   # Gerador de gabaritos
├── routes/
│   ├── gabarito_routes.py    # Endpoints de gabaritos
│   ├── prova_routes.py       # Endpoints de provas
│   └── resultado_routes.py   # Endpoints de resultados
├── data/               # Dados persistentes
├── gabaritos_gerados/  # Gabaritos em PNG
├── requirements.txt    # Dependências
├── Dockerfile         # Containerização
└── .env.example       # Exemplo de variáveis de ambiente
```

## 🚀 Quick Start

### 1. Com Python local

```bash
# Entrar no diretório do backend
cd backend

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
python main.py
```

API estará disponível em: `http://localhost:8000`

### 2. Com Docker

```bash
# Rodar a partir da raiz do projeto
docker-compose up backend

# API estará em: http://localhost:8000
```

## 📚 Endpoints

### Health Check

```bash
GET /health
# Resposta: { "status": "ok", "message": "TEstify Backend está funcionando" }
```

### Gabaritos

```bash
# Criar gabarito
POST /api/gabaritos
Content-Type: application/json

{
  "titulo": "Prova de Matemática",
  "num_questoes": 50,
  "alternativas": ["A", "B", "C", "D", "E"],
  "respostas_corretas": ["A", "C", "B", "D", "E", ...],
  "descricao": "Prova do bimestre"
}

# Listar gabaritos
GET /api/gabaritos

# Obter gabarito específico
GET /api/gabaritos/{gabarito_id}

# Atualizar gabarito
PUT /api/gabaritos/{gabarito_id}

# Deletar gabarito
DELETE /api/gabaritos/{gabarito_id}
```

### Provas

```bash
# Submeter prova (multipart/form-data)
POST /api/provas
- gabarito_id: 1
- nome_aluno: "João Silva"
- matricula_aluno: "202312345"
- turma_aluno: "3ºA"
- imagem: <arquivo.jpg>

# Listar provas
GET /api/provas

# Obter prova específica
GET /api/provas/{prova_id}

# Deletar prova
DELETE /api/provas/{prova_id}
```

### Resultados

```bash
# Criar resultado de correção
POST /api/resultados
Content-Type: application/json

{
  "prova_id": 1,
  "gabarito_id": 1,
  "respostas_aluno": ["A", "C", "B", "D", "E", ...]
}

# Listar resultados
GET /api/resultados

# Obter resultado específico
GET /api/resultados/{resultado_id}

# Obter estatísticas de um gabarito
GET /api/resultados/gabarito/{gabarito_id}/estatisticas

# Deletar resultado
DELETE /api/resultados/{resultado_id}
```

## 🔧 Configuração

Crie um arquivo `.env` na pasta `backend/` (baseado em `.env.example`):

```env
HOST=0.0.0.0
PORT=8000
DEBUG=True
DATABASE_URL=sqlite:///./data/testify.db
CORS_ORIGINS=["*"]
MAX_UPLOAD_SIZE=10485760
UPLOAD_DIR=./data/uploads
```

## 📖 Documentação Interativa

Após iniciar o servidor:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testando

```bash
# Testar health check
curl http://localhost:8000/health

# Criar gabarito
curl -X POST http://localhost:8000/api/gabaritos \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Teste",
    "num_questoes": 5,
    "alternativas": ["A", "B", "C", "D", "E"],
    "respostas_corretas": ["A", "C", "B", "D", "E"]
  }'
```

## 🐳 Docker

```bash
# Build da imagem
docker build -t testify-backend ./backend

# Rodar container
docker run -p 8000:8000 testify-backend

# Com docker-compose
docker-compose up backend
docker-compose down
```

## 📝 Próximos Passos

- [ ] Implementar OCR real com Tesseract
- [ ] Adicionar banco de dados PostgreSQL
- [ ] Autenticação JWT
- [ ] Rate limiting
- [ ] Testes unitários
- [ ] CI/CD pipeline
- [ ] Cache com Redis
- [ ] Logs centralizados

## 🤝 Contribuindo

Veja [CONTRIBUTING.md](../CONTRIBUTING.md)

## 📄 Licença

MIT
