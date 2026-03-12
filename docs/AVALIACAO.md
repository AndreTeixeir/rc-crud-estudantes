# Avaliação da Primeira Parte — Raciocínio Computacional

**Disciplina:** Raciocínio Computacional  
**Atividade:** Somativa 1 — Semana 4  
**Autor:** André Teixeira  
**Instituição:** Pontifícia Universidade Católica do Paraná (PUCPR)  

---

## 1. Objetivo da Atividade

A primeira parte da atividade somativa solicitou a implementação das funcionalidades de **inclusão** e **listagem de estudantes**, utilizando listas e entradas de dados. O sistema deveria manter a estrutura de navegação por menus já desenvolvida nas semanas anteriores, com as seguintes características:

- Perguntar apenas o nome do estudante ao usuário
- Armazenar os nomes em uma lista
- Utilizar estrutura de repetição para percorrer a lista na listagem
- Exibir mensagem `"Não há estudantes cadastrados"` quando a lista estiver vazia
- Exibir `"EM DESENVOLVIMENTO"` para funcionalidades ainda não implementadas

---

## 2. Avaliação de Conformidade

A tabela abaixo apresenta a análise de cada requisito solicitado na atividade:

| Requisito Solicitado | Status | Evidência no Código |
|---|---|---|
| Funcionalidade de incluir estudante | **Atendido** | Função `incluir_estudante()` |
| Funcionalidade de listar estudantes | **Atendido** | Função `listar_estudantes()` |
| Apenas nome perguntado ao usuário | **Atendido** | `input("Digite o nome do estudante: ")` |
| Armazenamento em lista | **Atendido** | `estudantes = []` + `estudantes.append(nome)` |
| Estrutura de repetição na listagem | **Atendido** | `for estudante in estudantes:` |
| Mensagem quando lista vazia | **Atendido** | `"Não há estudantes cadastrados."` |
| Mensagem "EM DESENVOLVIMENTO" no menu principal | **Atendido** | Opções 2, 3, 4 e 5 do menu principal |
| Mensagem "EM DESENVOLVIMENTO" no menu de estudantes | **Atendido** | Opções 3 e 4 do menu de estudantes |
| Código comentado | **Atendido** | Docstrings e comentários em todas as funções |
| Nome e curso no cabeçalho | **Atendido** | Comentários no início do arquivo |
| Arquivo único `.py` | **Atendido** | `rc_somativa_v1.py` |

**Resultado:** Todos os requisitos da Parte 1 foram atendidos.

---

## 3. Melhorias Implementadas na Versão Aprimorada

A versão aprimorada (`rc_somativa_v1.py`) mantém total conformidade com os requisitos e adiciona as seguintes melhorias em relação à versão original entregue:

### 3.1 Validação de Dados

A função `validar_nome()` foi adicionada para garantir que o nome informado seja válido antes de ser incluído na lista. As regras de validação aplicadas são:

- O nome não pode estar vazio ou conter apenas espaços em branco
- O nome deve ter no mínimo 3 caracteres
- O nome não pode ultrapassar 100 caracteres

### 3.2 Verificação de Duplicidade

A função `nome_duplicado()` verifica se um estudante com o mesmo nome já foi cadastrado, realizando a comparação sem distinção entre letras maiúsculas e minúsculas. Isso evita registros duplicados como "Lucas" e "lucas".

### 3.3 Interface Visual Aprimorada

Foram adicionadas as funções `exibir_cabecalho()` e `aguardar_enter()` para melhorar a experiência do usuário no terminal, proporcionando uma navegação mais clara e organizada entre as telas do sistema.

### 3.4 Tratamento de Exceções Expandido

Além do `EOFError` já tratado na versão original, a versão aprimorada também captura `KeyboardInterrupt` (Ctrl+C) durante a inclusão de estudantes, evitando que o programa encerre abruptamente.

### 3.5 Contador na Listagem

A listagem de estudantes passou a exibir o total de registros cadastrados e a numerar cada entrada, facilitando a visualização quando há muitos estudantes.

---

## 4. Análise de Qualidade do Código

### 4.1 Pontos Positivos

O código original demonstra boa compreensão dos conceitos fundamentais de Python. A separação das responsabilidades em funções distintas (`menu_principal`, `menu_estudantes`, `incluir_estudante`, `listar_estudantes`) segue o princípio de **responsabilidade única**, tornando o código mais legível e manutenível. A presença de docstrings em todas as funções é uma prática excelente para documentação do código.

### 4.2 Pontos de Atenção

A principal limitação da Parte 1 é a **ausência de persistência de dados**: ao encerrar o programa, todos os estudantes cadastrados são perdidos. Este ponto será abordado na Parte 2, onde será implementado o salvamento em arquivo. Adicionalmente, a estrutura de dados utilizada (lista de strings) é adequada para esta fase, mas precisará ser expandida para dicionários na Parte 2, quando múltiplos atributos por entidade serão necessários.

---

## 5. Checklist Final da Disciplina

Com base nos requisitos da Parte 2 (checklist final), a tabela abaixo mostra o status atual de cada item:

| Item do Checklist Final | Status na Parte 1 |
|---|---|
| CRUD completo para Estudantes | Parcial (incluir e listar) |
| CRUD completo para Professores | Não iniciado |
| CRUD completo para Disciplinas | Não iniciado |
| CRUD completo para Turmas | Não iniciado |
| CRUD completo para Matrículas | Não iniciado |
| Estruturas condicionais (`if/elif/else`) | Implementado |
| Estruturas de repetição (`for/while`) | Implementado |
| Estruturas de dados compostas (listas) | Implementado |
| Persistência em arquivo | Não iniciado |
| Funções para modularização | Implementado |
| Validações e tratamento de exceções | Parcial |

---

## 6. Recomendações para a Parte 2

Para a próxima entrega, recomenda-se:

1. **Expandir a estrutura de dados** de lista de strings para lista de dicionários, permitindo armazenar múltiplos atributos por estudante (código, nome, etc.)
2. **Implementar persistência em arquivo** utilizando JSON para salvar e carregar os dados entre execuções
3. **Criar funções genéricas** para operações CRUD que possam ser reutilizadas entre os diferentes módulos (estudantes, professores, disciplinas, turmas e matrículas)
4. **Implementar as operações de atualizar e excluir** para estudantes antes de expandir para os demais módulos
5. **Adicionar validações específicas** para cada tipo de dado (código numérico, CPF, etc.)
