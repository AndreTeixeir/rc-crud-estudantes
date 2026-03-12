# Sistema de Gestão Acadêmica — CRUD em Python

**Disciplina:** Raciocínio Computacional  
**Curso:** Inteligência Artificial Aplicada  
**Autor:** André Teixeira  
**Instituição:** Pontifícia Universidade Católica do Paraná (PUCPR)  

---

## Descrição

Este projeto consiste no desenvolvimento de um sistema de gestão acadêmica em Python, com interface via terminal (CLI). O sistema implementa operações de **CRUD** (Create, Read, Update, Delete) para os principais módulos de uma instituição de ensino: estudantes, professores, disciplinas, turmas e matrículas.

O projeto está sendo desenvolvido em etapas ao longo da disciplina de Raciocínio Computacional, aplicando progressivamente os conceitos estudados em cada semana.

---

## Funcionalidades

<<<<<<< HEAD
### Parte 1 — Semana 4
=======
### Parte 1 — Semana 4 (Versão Atual)
>>>>>>> 6404170967c0c66de98a66afb155a59642702110

A primeira entrega contempla a estrutura de navegação completa do sistema e as funcionalidades do módulo de **Estudantes**:

| Funcionalidade | Status |
|---|---|
| Menu principal com navegação | Implementado |
| Menu de operações de estudantes | Implementado |
| Incluir estudante | Implementado |
| Listar estudantes | Implementado |
| Atualizar estudante | Em desenvolvimento |
| Excluir estudante | Em desenvolvimento |
| Módulo de Professores | Em desenvolvimento |
| Módulo de Disciplinas | Em desenvolvimento |
| Módulo de Turmas | Em desenvolvimento |
| Módulo de Matrículas | Em desenvolvimento |

<<<<<<< HEAD
### Parte 2 — Semana 8 (Versão Final)

A segunda entrega expande o sistema com:

- CRUD completo para todos os módulos (Professores, Disciplinas, Turmas e Matrículas)
- Persistência de dados em arquivo JSON
- Validação avançada de dados e referências
- Funções genéricas reutilizáveis entre módulos
=======
### Parte 2 — Semana 8 (Próxima Entrega)

A segunda entrega expandirá o sistema com:

- CRUD completo para todos os módulos (Professores, Disciplinas, Turmas e Matrículas)
- Persistência de dados em arquivo
- Validação avançada de dados
- Reutilização de funções genéricas entre módulos
>>>>>>> 6404170967c0c66de98a66afb155a59642702110

---

## Estrutura do Projeto

```
rc-crud-estudantes/
│
<<<<<<< HEAD
├── rc_somativa_v1.py       # Código-fonte (Parte 1)
├── rc_somativa_v2.py       # Código-fonte (Parte 2 - Final)
├── README.md               # Documentação principal do projeto
├── dados/                  # Arquivos JSON de persistência (gerados automaticamente)
└── docs/
    ├── AVALIACAO.md        # Avaliação e análise da Parte 1
    ├── PARTE2.md           # Documentação da Parte 2
=======
├── rc_somativa_v1.py       # Código-fonte principal (Parte 1)
├── README.md               # Documentação principal do projeto
└── docs/
    ├── AVALIACAO.md        # Avaliação e análise da Parte 1
>>>>>>> 6404170967c0c66de98a66afb155a59642702110
    └── CHANGELOG.md        # Histórico de alterações
```

---

## Como Executar

### Pré-requisitos

- Python 3.6 ou superior instalado
- Nenhuma dependência externa necessária

### Execução

<<<<<<< HEAD
**Parte 1:**
=======
>>>>>>> 6404170967c0c66de98a66afb155a59642702110
```bash
python rc_somativa_v1.py
```

<<<<<<< HEAD
**Parte 2 (Final):**
```bash
python rc_somativa_v2.py
```

Ou, em sistemas onde Python 3 é chamado explicitamente:

```bash
python3 rc_somativa_v2.py
=======
Ou, em sistemas onde Python 3 é chamado explicitamente:

```bash
python3 rc_somativa_v1.py
>>>>>>> 6404170967c0c66de98a66afb155a59642702110
```

---

## Exemplo de Uso

Ao iniciar o programa, o menu principal é exibido:

```
==================================================
          SISTEMA DE GESTÃO ACADÊMICA
==================================================

  1. Estudantes
  2. Professores   (EM DESENVOLVIMENTO)
  3. Disciplinas   (EM DESENVOLVIMENTO)
  4. Turmas        (EM DESENVOLVIMENTO)
  5. Matrículas    (EM DESENVOLVIMENTO)
  0. Sair

Escolha uma opção:
```

Ao selecionar a opção **1 - Estudantes**, o submenu é exibido:

```
==================================================
        ESTUDANTES - MENU DE OPERAÇÕES
==================================================

  1. Incluir Estudante
  2. Listar Estudantes
  3. Atualizar Estudante  (EM DESENVOLVIMENTO)
  4. Excluir Estudante    (EM DESENVOLVIMENTO)
  0. Voltar ao Menu Principal

Escolha uma opção:
```

---

## Conceitos Aplicados

O projeto aplica os seguintes conceitos de Raciocínio Computacional estudados na disciplina:

| Conceito | Aplicação no Código |
|---|---|
| Estruturas condicionais (`if/elif/else`) | Navegação entre menus e validações |
| Estruturas de repetição (`while/for`) | Loop dos menus e iteração sobre a lista |
| Listas | Armazenamento dos nomes de estudantes |
| Funções | Modularização das funcionalidades |
| Tratamento de exceções (`try/except`) | Captura de `EOFError` e `KeyboardInterrupt` |
| Entrada de dados (`input`) | Leitura de opções e nomes do usuário |

---

## Histórico de Versões

Consulte o arquivo [CHANGELOG.md](docs/CHANGELOG.md) para o histórico completo de alterações.

---

## Avaliação

Para a análise detalhada de conformidade com os requisitos e as melhorias aplicadas, consulte o arquivo [AVALIACAO.md](docs/AVALIACAO.md).
