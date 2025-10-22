# 📱 TEstify - Seu Assistente de Avaliação

> Uma aplicação moderna e intuitiva para professores criarem, gerenciarem e corrigirem avaliações com facilidade.

**Frontend**: React Native + Expo  
**Backend**: FastAPI + Python  
**Deployment**: Docker + Docker Compose

---

## 🎯 Sobre o Projeto

**TEstify** é uma solução completa para educadores que desejam:

- ✅ Criar templates de avaliações personalizadas
- ✅ Corrigir provas de forma rápida e eficiente
- ✅ Gerar relatórios detalhados de desempenho
- ✅ Acompanhar o progresso dos alunos
- ✅ Automatizar a geração de gabaritos em PDF/PNG

Desenvolvido com **React Native**, **Expo** e **FastAPI**, funciona perfeitamente em Android, iOS, Web e pode ser deployado em qualquer servidor.

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────┐
│   Frontend (React Native + Expo)            │
│   - SplashScreen / HomeScreen               │
│   - CreateTemplateScreen (Criar gabaritos)  │
│   - CorrectorScreen (Corrigir provas)       │
│   - ReportsScreen (Visualizar resultados)   │
└────────────┬────────────────────────────────┘
             │ HTTP/REST API
             ▼
┌─────────────────────────────────────────────┐
│   Backend API (FastAPI + Python)            │
│   ├─ /api/gabaritos (CRUD)                  │
│   ├─ /api/provas (Upload + Storage)         │
│   └─ /api/resultados (Correção + Stats)     │
│                                             │
│   Features:                                 │
│   - Geração de Gabaritos (PIL/Pillow)      │
│   - Upload de Provas (Multipart)            │
│   - Processamento de Imagens (OpenCV)      │
│   - OCR (Tesseract)                         │
│   - Cálculo Automático de Notas             │
└────────────┬────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│   Persistência & Storage                    │
│   - JSON Files (desenvolvimento)            │
│   - SQLite/PostgreSQL (produção)            │
│   - File Storage (Uploads de provas)        │
│   - PNG Storage (Gabaritos gerados)         │
└─────────────────────────────────────────────┘
```

---

## 🔧 Stack Técnico

### Frontend

- **React Native** - Framework mobile cross-platform
- **Expo** - Plataforma para desenvolvimento rápido
- **TypeScript** - Type safety
- **Reanimated** - Animações performáticas
- **React Native Paper** - Componentes UI

### Backend

- **FastAPI** - Framework web assíncrono de alta performance
- **Pydantic** - Validação de dados robusto
- **Pillow (PIL)** - Geração de gabaritos em PNG
- **OpenCV** - Processamento de imagens
- **Tesseract OCR** - Reconhecimento óptico de caracteres
- **SQLAlchemy** - ORM para banco de dados

### DevOps & Deployment

- **Docker** - Containerização
- **Docker Compose** - Orquestração local
- **Uvicorn** - Servidor ASGI

---

## 🚀 Quick Start

### Opção 1: Frontend Apenas (Local)

Perfeito para desenvolvimento do frontend:

```bash
# Instalar dependências
npm install

# Iniciar servidor de desenvolvimento
npm start
```

Depois:

- **Expo Go**: Escaneie o QR code com seu smartphone
- **Web**: Pressione `w` no terminal
- **Simulador Android**: Pressione `a`
- **Simulador iOS**: Pressione `i`

### Opção 2: Frontend + Backend (Recomendado)

Ambiente completo com frontend web e backend:

```bash
# A partir da raiz do projeto
docker-compose up
```

Acesse:

- **Frontend Web**: http://localhost:3000 (quando houver)
- **Backend API**: http://localhost:8000
- **Swagger API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Opção 3: Backend Apenas

Para desenvolver apenas a API:

```bash
cd backend

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
python main.py
```

API disponível em: http://localhost:8000

---

## 📚 Funcionalidades Principais

### 🏠 Tela Inicial

- Interface amigável com opções de navegação
- Acesso rápido às principais funções
- Design moderno com gradientes

### 📋 Criar Gabarito

- Defina título da avaliação
- Configure número de questões
- Adicione gabarito (respostas corretas)
- **Gera automaticamente PDF/PNG formatado**
- Salve templates para reutilização

### 📷 Corrigir Provas

- Captura e processamento de imagens
- Reconhecimento automático de respostas (OCR)
- Entrada de dados do aluno (nome, matrícula, turma)
- Cálculo automático de notas

### 📊 Relatórios

- Visualize resultados por gabarito
- Histórico completo de correções
- Informações detalhadas do aluno
- **Estatísticas de desempenho**
  - Questão mais errada
  - Taxa de acerto média
  - Distribuição de notas

---

## 🛠️ Scripts Disponíveis

```bash
# Frontend
npm start              # Inicia desenvolvimento Expo
npm run start:web     # Inicia versão web
npm run tsc          # Verifica tipos TypeScript

# Backend
cd backend && python main.py  # Inicia API

# Docker
docker-compose up             # Inicia todos os serviços
docker-compose down           # Para todos os serviços
docker-compose logs backend   # Ver logs do backend
```

---

## 📁 Estrutura do Projeto

```
meuPrimeiroApp/
├── frontend/
│   ├── App.js                      # Componente principal
│   ├── index.js                    # Entry point
│   ├── SplashScreen.js
│   ├── HomeScreen.js
│   ├── CreateTemplateScreen.js
│   ├── CorrectorScreen.js
│   ├── ReportsScreen.js
│   ├── EmptyState.js
│   ├── assets/                     # Imagens e recursos
│   ├── components/                 # Componentes reutilizáveis
│   ├── hooks/                      # Custom React hooks
│   ├── constants/                  # Constantes da aplicação
│   └── package.json
│
├── backend/                        # ⭐ API REST
│   ├── main.py                     # Aplicação FastAPI
│   ├── schemas.py                  # Modelos Pydantic
│   ├── utils_gabarito.py          # Gerador de gabaritos
│   ├── routes/
│   │   ├── gabarito_routes.py      # CRUD de gabaritos
│   │   ├── prova_routes.py         # Upload de provas
│   │   └── resultado_routes.py     # Cálculo de resultados
│   ├── data/                       # Dados persistentes
│   ├── gabaritos_gerados/          # Gabaritos em PNG
│   ├── requirements.txt            # Dependências Python
│   ├── Dockerfile                  # Containerização
│   ├── .env.example                # Variáveis de ambiente
│   └── README.md                   # Documentação do backend
│
├── docker-compose.yml              # Orquestração
├── README.md                       # Este arquivo
├── CONTRIBUTING.md                 # Guia de contribuição
├── CHANGELOG.md                    # Histórico de versões
└── FAQ.md                          # Perguntas frequentes
```

---

## 🎨 Design & UI

- **Cores Principais**: Azul-acinzentado (#346a74) e Turquesa (#a1d5d1)
- **Tipografia**: Fonte do sistema
- **Ícones**: Material Community Icons
- **Gradientes**: Expo Linear Gradient
- **Layout**: Responsivo para mobile, tablet e web

---

## 📡 API REST - Principais Endpoints

### Health Check

```bash
GET /health
```

### Gabaritos

```bash
POST   /api/gabaritos              # Criar
GET    /api/gabaritos              # Listar
GET    /api/gabaritos/{id}         # Obter
PUT    /api/gabaritos/{id}         # Atualizar
DELETE /api/gabaritos/{id}         # Deletar
```

### Provas

```bash
POST   /api/provas                 # Submeter prova
GET    /api/provas                 # Listar
GET    /api/provas/{id}            # Obter
DELETE /api/provas/{id}            # Deletar
```

### Resultados

```bash
POST   /api/resultados             # Criar resultado
GET    /api/resultados             # Listar
GET    /api/resultados/{id}        # Obter
GET    /api/resultados/gabarito/{id}/estatisticas  # Estatísticas
DELETE /api/resultados/{id}        # Deletar
```

Veja [backend/README.md](./backend/README.md) para documentação completa.

---

## 📱 Compatibilidade

- ✅ **Android**: 5.0+
- ✅ **iOS**: 12.0+
- ✅ **Web**: Todos os navegadores modernos
- ✅ **Docker**: Qualquer SO com Docker instalado

---

## 🐛 Troubleshooting

### Frontend

**Erro: "Cannot find module"**

```bash
rm -rf node_modules package-lock.json
npm install
npm start
```

**Erro de asset não encontrado**

- Verifique se os arquivos existem em `assets/images/`
- Use caminho correto: `./assets/images/filename.png`

### Backend

**Erro: "ModuleNotFoundError"**

```bash
pip install -r requirements.txt
```

**Erro ao conectar com API**

- Verifique se o backend está rodando: `http://localhost:8000/health`
- Confirme o CORS está configurado para aceitar seu domínio

---

## 🚀 Deploy em Produção

### Docker Hub

```bash
docker build -t seu-usuario/testify-backend ./backend
docker push seu-usuario/testify-backend
```

### Railway / Heroku / AWS

Veja [backend/README.md](./backend/README.md) para mais detalhes.

---

## 📝 Commits Recentes

- ✅ feat: add complete backend API with FastAPI
- ✅ fix: switch from expo-router to custom App.js
- ✅ docs: update README with comprehensive documentation
- ✅ feat: add CONTRIBUTING.md, CHANGELOG.md, FAQ.md

---

## 📊 Roadmap

- [ ] Integração completa OCR (Tesseract)
- [ ] Autenticação JWT
- [ ] PostgreSQL em produção
- [ ] Exportação de relatórios em PDF
- [ ] Dashboard de estatísticas
- [ ] Sincronização na nuvem
- [ ] Mobile app nativa compilada
- [ ] Testes automatizados
- [ ] CI/CD pipeline

---

## 👨‍💻 Desenvolvimento

### Configurar Ambiente Local

```bash
# Frontend
npm install
npm start

# Backend (em outro terminal)
cd backend
pip install -r requirements.txt
python main.py
```

### Contribuir

Veja [CONTRIBUTING.md](./CONTRIBUTING.md) para diretrizes completas.

---

## 📄 Licença

Este projeto está disponível sob a licença MIT.

---

## 🤝 Comunidade

- **Issues**: https://github.com/LevyTavares/meuPrimeiroApp/issues
- **Discussões**: https://github.com/LevyTavares/meuPrimeiroApp/discussions
- **Pull Requests**: Contribuições são bem-vindas!

---

**Desenvolvido com ❤️ para educadores que se importam com a qualidade da avaliação.** 🎓
