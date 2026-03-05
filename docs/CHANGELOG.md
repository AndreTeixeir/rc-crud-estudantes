# Histórico de Alterações

Todas as alterações relevantes neste projeto serão documentadas neste arquivo.

O formato segue as convenções do [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [1.0.0] — 2024-11-16

### Adicionado

- Estrutura de navegação por menus (menu principal e menu de estudantes)
- Funcionalidade de **inclusão de estudante** com validação de entrada S/N
- Funcionalidade de **listagem de estudantes** com mensagem para lista vazia
- Mensagem `"EM DESENVOLVIMENTO"` para funcionalidades futuras nos menus
- Tratamento de `EOFError` para execução em ambientes automatizados
- Docstrings e comentários em todas as funções
- Cabeçalho com nome do autor e curso

### Melhorias Aplicadas (v1.0 — versão aprimorada)

- Adicionada validação de nome (vazio, mínimo de 3 caracteres, máximo de 100 caracteres)
- Adicionada verificação de duplicidade de nomes (case-insensitive)
- Adicionada função `exibir_cabecalho()` para melhor formatação visual
- Adicionada função `aguardar_enter()` para navegação mais fluida
- Adicionada função `limpar_tela()` para melhor experiência no terminal
- Adicionado contador de estudantes na listagem
- Adicionada numeração dos registros na listagem
- Expandido tratamento de exceções para incluir `KeyboardInterrupt`

---

## [2.0.0] — Previsto para Semana 8

### Planejado

- CRUD completo (incluir, listar, atualizar, excluir) para todos os módulos:
  - Professores (código, nome, CPF)
  - Disciplinas (código, nome)
  - Turmas (código, código do professor, código da disciplina)
  - Matrículas (código da turma, código do estudante)
- Persistência de dados em arquivo (JSON)
- Validação de unicidade de códigos para turmas e matrículas
- Funções genéricas e reutilizáveis entre módulos
- Estrutura de dados expandida para dicionários
