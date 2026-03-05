# Instruções para Upload no GitHub

Este documento fornece um passo a passo para fazer o upload deste projeto para o GitHub.

---

## Pré-requisitos

- Git instalado no seu computador ([Download](https://git-scm.com/))
- Conta no GitHub ([Criar conta](https://github.com/signup))
- Terminal/Prompt de Comando aberto na pasta do projeto

---

## Passo 1: Criar um Repositório no GitHub

1. Acesse [https://github.com/new](https://github.com/new)
2. Preencha os campos:
   - **Repository name:** `rc-crud-estudantes`
   - **Description:** `Sistema de Gestão Acadêmica - CRUD em Python - Raciocínio Computacional (PUCPR)`
   - **Visibility:** Selecione `Public`
3. Clique em **Create repository**

---

## Passo 2: Configurar Git Localmente

Abra o terminal na pasta do projeto e execute os seguintes comandos:

### 2.1 Configurar identidade (se não tiver feito antes)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

### 2.2 Inicializar repositório local

```bash
git init
```

### 2.3 Adicionar arquivo .gitignore

O arquivo `.gitignore` já está incluído no projeto. Ele será adicionado automaticamente no próximo passo.

---

## Passo 3: Fazer o Primeiro Commit

Execute os seguintes comandos na ordem:

```bash
# Adicionar todos os arquivos ao staging
git add .

# Criar o primeiro commit
git commit -m "Primeira parte do projeto - CRUD de Estudantes (Semana 4)"

# Verificar o status (opcional)
git status
```

---

## Passo 4: Conectar ao Repositório Remoto e Fazer Push

Copie a URL do repositório que você criou no GitHub (será algo como `https://github.com/seu-usuario/rc-crud-estudantes.git`).

Execute os comandos:

```bash
# Adicionar o repositório remoto
git remote add origin https://github.com/seu-usuario/rc-crud-estudantes.git

# Renomear branch para 'main' (padrão do GitHub)
git branch -M main

# Fazer o push para o GitHub
git push -u origin main
```

---

## Passo 5: Verificar no GitHub

1. Acesse seu repositório em `https://github.com/seu-usuario/rc-crud-estudantes`
2. Verifique se todos os arquivos foram enviados corretamente
3. Confirme que o README.md está sendo exibido na página principal

---

## Próximos Passos (Parte 2)

Quando chegar a hora de desenvolver a Parte 2, você pode:

1. Criar uma branch `develop` para desenvolvimento:
   ```bash
   git checkout -b develop
   ```

2. Criar branches de feature para cada funcionalidade:
   ```bash
   git checkout -b feature/professores
   git checkout -b feature/disciplinas
   git checkout -b feature/turmas
   git checkout -b feature/matriculas
   ```

3. Fazer commits regularmente:
   ```bash
   git add .
   git commit -m "Descrição da alteração"
   git push origin feature/seu-feature
   ```

4. Fazer merge na branch `develop` e depois em `main` quando concluído.

---

## Dúvidas Frequentes

**P: E se eu cometer um erro?**  
R: Você pode desfazer o último commit com `git reset --soft HEAD~1` antes do push. Após fazer push, consulte a documentação do GitHub sobre como reverter commits.

**P: Como faço para atualizar o repositório depois?**  
R: Após fazer alterações, execute:
```bash
git add .
git commit -m "Descrição das alterações"
git push origin main
```

**P: Posso usar GitHub Desktop em vez da linha de comando?**  
R: Sim! GitHub Desktop oferece uma interface gráfica para fazer as mesmas operações.

---

## Recursos Úteis

- [Documentação do Git](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)
- [Git Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
