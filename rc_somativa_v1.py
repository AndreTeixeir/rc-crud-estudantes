# Nome: ANDRÉ TEIXEIRA
# Curso: INTELIGENCIA ARTIFICIAL APLICADA
# Atividade: CRUD ESTUDANTES - RACIOCÍNIO COMPUTACIONAL
# Versão: 1.0 - Parte 1 (Semana 4)
# Descrição: Sistema de gerenciamento de estudantes com operações de inclusão e listagem.

import os

# Lista para armazenar os nomes dos estudantes
estudantes = []

# ─────────────────────────────────────────────
# FUNÇÕES UTILITÁRIAS
# ─────────────────────────────────────────────

def limpar_tela():
    """Limpa a tela do console para melhor visualização."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(titulo):
    """
    Exibe um cabeçalho formatado para cada seção do sistema.
    
    Parâmetros:
        titulo (str): Título a ser exibido no cabeçalho.
    """
    print("\n" + "=" * 50)
    print(f"  {titulo.center(46)}")
    print("=" * 50)

def aguardar_enter():
    """Aguarda o usuário pressionar ENTER para continuar."""
    input("\nPressione ENTER para continuar.")

def validar_nome(nome):
    """
    Valida o nome do estudante informado pelo usuário.
    
    Parâmetros:
        nome (str): Nome a ser validado.
    
    Retorna:
        tuple: (bool, str) onde bool indica se é válido e str é a mensagem.
    """
    if not nome or not nome.strip():
        return False, "O nome não pode estar vazio."
    if len(nome.strip()) < 3:
        return False, "O nome deve ter pelo menos 3 caracteres."
    if len(nome.strip()) > 100:
        return False, "O nome não pode ter mais de 100 caracteres."
    return True, "Válido"

def nome_duplicado(nome):
    """
    Verifica se o nome já existe na lista de estudantes (sem distinção de maiúsculas/minúsculas).
    
    Parâmetros:
        nome (str): Nome a ser verificado.
    
    Retorna:
        bool: True se o nome já existir, False caso contrário.
    """
    return nome.strip().lower() in [e.lower() for e in estudantes]

# ─────────────────────────────────────────────
# FUNÇÕES DE ESTUDANTES
# ─────────────────────────────────────────────

def incluir_estudante():
    """
    Permite ao usuário incluir um ou mais estudantes na lista,
    com validação de dados e verificação de duplicidade.
    """
    exibir_cabecalho("INCLUSÃO DE ESTUDANTE")

    while True:
        try:
            nome = input("\nDigite o nome do estudante: ").strip()

            # Validação do nome
            valido, mensagem = validar_nome(nome)
            if not valido:
                print(f"[ERRO] {mensagem}")
                continue

            # Verificação de duplicidade
            if nome_duplicado(nome):
                print(f"[AVISO] O estudante '{nome}' já está cadastrado.")
                continuar = input("Deseja informar outro nome? (S/N): ").upper()
                while continuar not in ("S", "N"):
                    print("[ERRO] Opção inválida. Digite 'S' ou 'N'.")
                    continuar = input("Deseja informar outro nome? (S/N): ").upper()
                if continuar == "N":
                    break
                continue

            # Inclusão do estudante
            estudantes.append(nome.strip())
            print(f"[OK] Estudante '{nome}' incluído com sucesso.")

            # Pergunta se deseja incluir outro
            continuar = input("\nDeseja incluir outro estudante? (S/N): ").upper()
            while continuar not in ("S", "N"):
                print("[ERRO] Opção inválida. Digite 'S' ou 'N'.")
                continuar = input("Deseja incluir outro estudante? (S/N): ").upper()

            if continuar == "N":
                break

        except KeyboardInterrupt:
            print("\n\n[AVISO] Operação cancelada pelo usuário.")
            break

    aguardar_enter()

def listar_estudantes():
    """
    Exibe a lista de todos os estudantes cadastrados no sistema.
    Exibe mensagem informativa caso nenhum estudante esteja cadastrado.
    """
    exibir_cabecalho("LISTAGEM DE ESTUDANTES")

    if estudantes:
        print(f"\nTotal de estudantes cadastrados: {len(estudantes)}\n")
        for i, estudante in enumerate(estudantes, start=1):
            print(f"  {i:>3}. {estudante}")
    else:
        print("\nNão há estudantes cadastrados.")

    aguardar_enter()

# ─────────────────────────────────────────────
# MENUS
# ─────────────────────────────────────────────

def menu_estudantes():
    """
    Exibe o menu de operações do estudante e processa a opção escolhida pelo usuário.
    Retorna ao menu principal quando o usuário escolhe a opção 0.
    """
    while True:
        exibir_cabecalho("ESTUDANTES - MENU DE OPERAÇÕES")
        print()
        print("  1. Incluir Estudante")
        print("  2. Listar Estudantes")
        print("  3. Atualizar Estudante  (EM DESENVOLVIMENTO)")
        print("  4. Excluir Estudante    (EM DESENVOLVIMENTO)")
        print("  0. Voltar ao Menu Principal")
        print()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            incluir_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao in ["3", "4"]:
            print("\n[INFO] Funcionalidade EM DESENVOLVIMENTO.")
            aguardar_enter()
        elif opcao == "0":
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")
            aguardar_enter()

def menu_principal():
    """
    Exibe o menu principal do sistema e processa a opção escolhida pelo usuário.
    Mantém o loop até que o usuário escolha a opção de sair (0).
    """
    while True:
        try:
            exibir_cabecalho("SISTEMA DE GESTÃO ACADÊMICA")
            print()
            print("  1. Estudantes")
            print("  2. Professores   (EM DESENVOLVIMENTO)")
            print("  3. Disciplinas   (EM DESENVOLVIMENTO)")
            print("  4. Turmas        (EM DESENVOLVIMENTO)")
            print("  5. Matrículas    (EM DESENVOLVIMENTO)")
            print("  0. Sair")
            print()

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                menu_estudantes()
            elif opcao in ["2", "3", "4", "5"]:
                print("\n[INFO] Funcionalidade EM DESENVOLVIMENTO.")
                aguardar_enter()
            elif opcao == "0":
                print("\nSaindo do sistema. Até logo!")
                break
            else:
                print("\n[ERRO] Opção inválida. Tente novamente.")
                aguardar_enter()

        except EOFError:
            break  # Encerra o programa em caso de EOF (ex: execução automatizada)

# ─────────────────────────────────────────────
# PONTO DE ENTRADA
# ─────────────────────────────────────────────

try:
    menu_principal()
except EOFError:
    pass  # Ignora EOFError ao encerrar o programa
