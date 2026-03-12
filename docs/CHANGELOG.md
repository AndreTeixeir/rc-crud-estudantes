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

## [2.0.0] — 2025-03-05

### Adicionado

- CRUD completo (incluir, listar, atualizar, excluir) para Estudantes
- CRUD completo para Professores (código, nome, CPF)
- CRUD completo para Disciplinas (código, nome)
- CRUD completo para Turmas (código, código do professor, código da disciplina)
- Incluir, Listar e Excluir para Matrículas (código da turma, código do estudante)
- Persistência de dados em arquivos JSON na pasta `dados/`
- Carregamento automático dos dados na inicialização
- Validação de unicidade de códigos em todos os módulos
- Validação de referências ao criar turmas e matrículas
- Validação básica de CPF para professores
- Funções genéricas reutilizáveis entre módulos
- Estrutura de dados expandida para dicionários
- Geração automática de códigos sequenciais
