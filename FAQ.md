# ❓ FAQ - Perguntas Frequentes

## Instalação e Setup

### P: Como instalar o TEstify?

**R:**

```bash
git clone <repositório>
cd meuPrimeiroApp
npm install
npm start
```

### P: Preciso de um servidor backend?

**R:** Não! O TEstify funciona completamente offline. Todos os dados são armazenados localmente no dispositivo.

### P: Posso usar em iOS e Android?

**R:** Sim! Use Expo Go ou crie um build nativo. O app funciona perfeitamente em ambas plataformas.

---

## Uso da Aplicação

### P: Como criar um novo gabarito?

**R:**

1. Na tela inicial, toque em "Criar um Novo Gabarito"
2. Preencha o título da avaliação
3. Defina o número de questões
4. Configure as respostas corretas
5. Toque em "Salvar"

### P: Como corrigir uma prova?

**R:**

1. Na tela inicial, toque em "Corrigir Provas"
2. Selecione o gabarito
3. Capture ou selecione a imagem da prova
4. Informe dados do aluno
5. Verifique o resultado

### P: Os dados são salvos automaticamente?

**R:** Sim! Todos os gabaritos e relatórios são salvos automaticamente.

### P: Posso exportar os relatórios?

**R:** Atualmente os relatórios são visualizados no app. Exportação em PDF está planejada para versões futuras.

---

## Troubleshooting

### P: O app não abre em Expo Go

**R:**

```bash
# Limpe o cache
npm start --clear
# Ou reinstale tudo
rm -rf node_modules package-lock.json
npm install
npm start
```

### P: Erro "Cannot find module"

**R:**

- Verifique se todas as dependências estão instaladas: `npm install`
- Limpe o cache do Metro: `npm start --clear`

### P: A câmera não funciona

**R:**

- Verifique permissões no dispositivo (Configurações > Permissões)
- Use Expo Go para testar (oferece mais permissões)
- Crie um build nativo para produção

### P: Como resetar todos os dados?

**R:** Os dados são armazenados localmente. Para resetar, desinstale e reinstale o app.

---

## Desenvolvimento

### P: Como adicionar novas funcionalidades?

**R:** Veja [CONTRIBUTING.md](./CONTRIBUTING.md) para instruções completas.

### P: Posso modificar o design?

**R:** Sim! Edite os estilos em `styles` ou use `constants/theme.ts`.

### P: Como fazer debug?

**R:**

```bash
npm start
# Pressione 'j' para abrir o debugger
```

---

## Compatibilidade

### P: Qual é a versão mínima do Android?

**R:** Android 5.0 ou superior

### P: Qual é a versão mínima do iOS?

**R:** iOS 12.0 ou superior

### P: Funciona em navegadores Web?

**R:** Sim! Execute `npm run start:web`

---

## Performance e Otimização

### P: O app fica lento com muitos gabaritos?

**R:**

- O app é otimizado para até 1000+ gabaritos
- Se notar lentidão, você pode limpar dados antigos manualmente

### P: Qual é o tamanho do app?

**R:**

- APK (Android): ~50MB
- IPA (iOS): ~45MB

---

## Segurança

### P: Os dados são sincronizados na nuvem?

**R:** Não. Todos os dados permanecem no seu dispositivo, garantindo privacidade total.

### P: Como faço backup dos dados?

**R:** No iOS use iCloud, no Android use Google Drive (configuráveis nas Configurações do app).

---

## Suporte

### P: Onde reporto bugs?

**R:** Abra uma [issue no GitHub](https://github.com/LevyTavares/meuPrimeiroApp/issues)

### P: Como sugiro melhorias?

**R:** Envie uma issue com o label "enhancement"

### P: Como contribuo com código?

**R:** Veja [CONTRIBUTING.md](./CONTRIBUTING.md)

---

**Não encontrou sua pergunta? Abra uma issue!** 📝
