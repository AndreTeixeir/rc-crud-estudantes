# Documentação da Segunda Parte — Raciocínio Computacional

**Disciplina:** Raciocínio Computacional  
**Atividade:** Somativa Final — Semana 8  
**Autor:** André Teixeira  
**Curso:** Inteligência Artificial Aplicada  
**Instituição:** Pontifícia Universidade Católica do Paraná (PUCPR)  

---

## 1. Visão Geral

A segunda parte do projeto expande o sistema de gestão acadêmica desenvolvido na Parte 1, implementando o CRUD completo para todos os módulos do sistema e adicionando persistência de dados em arquivo. O sistema agora é capaz de gerenciar estudantes, professores, disciplinas, turmas e matrículas, mantendo os dados salvos entre as execuções do programa.

---

## 2. Novidades em Relação à Parte 1

A tabela abaixo resume as principais evoluções entre as duas versões do sistema:

| Aspecto | Parte 1 (v1.0) | Parte 2 (v2.0) |
|---|---|---|
| Módulos com CRUD | Apenas Estudantes (parcial) | Todos os 5 módulos (completo) |
| Operações disponíveis | Incluir e Listar | Incluir, Listar, Atualizar e Excluir |
| Estrutura de dados | Lista de strings | Lista de dicionários |
| Persistência | Não (dados em memória) | Sim (arquivos JSON) |
| Validação de dados | Básica (nome) | Avançada (nome, CPF, referências) |
| Verificação de duplicidade | Não | Sim (código e matrícula) |
| Relacionamentos | Não | Sim (turma referencia professor e disciplina) |

---

## 3. Estrutura de Dados

Cada módulo utiliza uma lista de dicionários para armazenar os registros. A estrutura de cada entidade é a seguinte:

| Módulo | Campos |
|---|---|
| Estudantes | `codigo` (int), `nome` (str) |
| Professores | `codigo` (int), `nome` (str), `cpf` (str) |
| Disciplinas | `codigo` (int), `nome` (str) |
| Turmas | `codigo` (int), `codigo_professor` (int), `codigo_disciplina` (int) |
| Matrículas | `codigo_turma` (int), `codigo_estudante` (int) |

---

## 4. Persistência em Arquivo

Os dados são salvos automaticamente em arquivos JSON sempre que uma operação de escrita (incluir, atualizar ou excluir) é realizada. Os arquivos são criados na subpasta `dados/` dentro do diretório do projeto.

| Arquivo | Conteúdo |
|---|---|
| `dados/estudantes.json` | Lista de estudantes |
| `dados/professores.json` | Lista de professores |
| `dados/disciplinas.json` | Lista de disciplinas |
| `dados/turmas.json` | Lista de turmas |
| `dados/matriculas.json` | Lista de matrículas |

Ao iniciar o programa, todos os dados são carregados automaticamente dos arquivos, garantindo que nenhuma informação seja perdida entre as execuções.

---

## 5. Funções Genéricas e Reutilização de Código

Uma das principais melhorias da Parte 2 é a criação de funções genéricas que são reutilizadas por todos os módulos, evitando repetição de código:

| Função | Descrição | Usada por |
|---|---|---|
| `gerar_proximo_codigo(lista)` | Gera o próximo código disponível | Todos os módulos |
| `codigo_existe(lista, codigo)` | Verifica se um código já existe | Todos os módulos |
| `encontrar_por_codigo(lista, codigo)` | Busca um registro pelo código | Todos os módulos |
| `incluir_registro(lista, registro, modulo)` | Inclui com validação de unicidade | Todos os módulos |
| `listar_registros(lista, nome, campos)` | Lista com formatação | Todos os módulos |
| `atualizar_registro(lista, codigo, dados, modulo)` | Atualiza e salva | Todos os módulos |
| `excluir_registro(lista, codigo, modulo)` | Exclui e salva | Todos os módulos |
| `salvar_em_arquivo(modulo, dados)` | Persiste em JSON | Todos os módulos |
| `carregar_de_arquivo(modulo)` | Carrega de JSON | Inicialização |

---

## 6. Validações Implementadas

O sistema realiza as seguintes validações antes de aceitar qualquer dado:

**Validação de Nome** — aplicada a estudantes, professores e disciplinas:
- O nome não pode estar vazio ou conter apenas espaços
- O nome deve ter no mínimo 3 caracteres
- O nome não pode ultrapassar 100 caracteres

**Validação de CPF** — aplicada ao cadastro de professores:
- O CPF deve conter exatamente 11 dígitos numéricos
- O formato aceito é `XXX.XXX.XXX-XX`

**Validação de Referências** — aplicada ao cadastro de turmas e matrículas:
- Ao criar uma turma, o sistema verifica se o professor e a disciplina informados existem
- Ao criar uma matrícula, o sistema verifica se a turma e o estudante informados existem

**Validação de Duplicidade** — aplicada a todos os módulos:
- Nenhum código pode ser duplicado dentro do mesmo módulo
- Uma matrícula não pode ser criada duas vezes para o mesmo par turma/estudante

---

## 7. Checklist de Conformidade com os Requisitos

| Item do Checklist | Status |
|---|---|
| CRUD completo para Estudantes | Implementado |
| CRUD completo para Professores | Implementado |
| CRUD completo para Disciplinas | Implementado |
| CRUD completo para Turmas | Implementado |
| Excluir e Listar para Matrículas | Implementado |
| Estruturas condicionais (`if/elif/else`) | Implementado |
| Estruturas de repetição (`for/while`) | Implementado |
| Estruturas de dados compostas (dicionários e listas) | Implementado |
| Persistência em arquivo (JSON) | Implementado |
| Funções para modularização | Implementado |
| Reutilização de funções entre módulos | Implementado |
| Validações e tratamento de exceções (`try/except`) | Implementado |
| Validação de unicidade de códigos | Implementado |

---

## 8. Como Executar

Siga os mesmos passos descritos no `README.md`, utilizando o arquivo `rc_somativa_v2.py`:

```bash
python rc_somativa_v2.py
```

Na primeira execução, a pasta `dados/` será criada automaticamente. Os arquivos JSON serão gerados conforme os dados forem cadastrados.

---

## 9. Fluxo de Uso Recomendado

Para utilizar o sistema corretamente, recomenda-se seguir a ordem abaixo ao cadastrar os dados pela primeira vez:

1. Cadastrar **Professores**
2. Cadastrar **Disciplinas**
3. Cadastrar **Estudantes**
4. Criar **Turmas** (associando professor e disciplina)
5. Criar **Matrículas** (associando turma e estudante)

Esta ordem garante que as referências necessárias já existam no momento do cadastro.
