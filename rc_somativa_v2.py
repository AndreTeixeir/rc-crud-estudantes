# Nome: ANDRÉ TEIXEIRA
# Curso: INTELIGENCIA ARTIFICIAL APLICADA
# Atividade: CRUD COMPLETO - RACIOCÍNIO COMPUTACIONAL
# Versão: 2.0 - Parte 2 (Semana 8)
# Descrição: Sistema completo de gestão acadêmica com CRUD para todos os módulos e persistência em arquivo.

import os
import json
from pathlib import Path

# ─────────────────────────────────────────────
# CONFIGURAÇÕES GLOBAIS
# ─────────────────────────────────────────────

DIRETORIO_DADOS = Path(__file__).parent / "dados"
ARQUIVOS = {
    "estudantes": DIRETORIO_DADOS / "estudantes.json",
    "professores": DIRETORIO_DADOS / "professores.json",
    "disciplinas": DIRETORIO_DADOS / "disciplinas.json",
    "turmas": DIRETORIO_DADOS / "turmas.json",
    "matriculas": DIRETORIO_DADOS / "matriculas.json"
}

# Estruturas de dados em memória
estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []

# ─────────────────────────────────────────────
# FUNÇÕES DE PERSISTÊNCIA EM ARQUIVO
# ─────────────────────────────────────────────

def criar_diretorio_dados():
    """Cria o diretório de dados se não existir."""
    DIRETORIO_DADOS.mkdir(exist_ok=True)

def salvar_em_arquivo(nome_modulo, dados):
    """
    Salva dados em arquivo JSON.
    
    Parâmetros:
        nome_modulo (str): Nome do módulo (estudantes, professores, etc.)
        dados (list): Lista de dados a serem salvos.
    """
    try:
        arquivo = ARQUIVOS.get(nome_modulo)
        if arquivo:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[ERRO] Falha ao salvar dados: {str(e)}")

def carregar_de_arquivo(nome_modulo):
    """
    Carrega dados de arquivo JSON.
    
    Parâmetros:
        nome_modulo (str): Nome do módulo.
    
    Retorna:
        list: Lista de dados carregados ou lista vazia se arquivo não existir.
    """
    try:
        arquivo = ARQUIVOS.get(nome_modulo)
        if arquivo and arquivo.exists():
            with open(arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"[ERRO] Falha ao carregar dados: {str(e)}")
    return []

def carregar_todos_dados():
    """Carrega todos os dados dos arquivos na inicialização."""
    global estudantes, professores, disciplinas, turmas, matriculas
    criar_diretorio_dados()
    estudantes = carregar_de_arquivo("estudantes")
    professores = carregar_de_arquivo("professores")
    disciplinas = carregar_de_arquivo("disciplinas")
    turmas = carregar_de_arquivo("turmas")
    matriculas = carregar_de_arquivo("matriculas")

# ─────────────────────────────────────────────
# FUNÇÕES GENÉRICAS DE CRUD
# ─────────────────────────────────────────────

def gerar_proximo_codigo(lista):
    """
    Gera o próximo código automático baseado no maior código existente.
    
    Parâmetros:
        lista (list): Lista de registros.
    
    Retorna:
        int: Próximo código disponível.
    """
    if not lista:
        return 1
    return max(reg.get("codigo", 0) for reg in lista) + 1

def codigo_existe(lista, codigo):
    """
    Verifica se um código já existe na lista.
    
    Parâmetros:
        lista (list): Lista de registros.
        codigo (int): Código a verificar.
    
    Retorna:
        bool: True se existe, False caso contrário.
    """
    return any(reg.get("codigo") == codigo for reg in lista)

def encontrar_por_codigo(lista, codigo):
    """
    Encontra um registro pelo código.
    
    Parâmetros:
        lista (list): Lista de registros.
        codigo (int): Código a procurar.
    
    Retorna:
        dict: Registro encontrado ou None.
    """
    for reg in lista:
        if reg.get("codigo") == codigo:
            return reg
    return None

def incluir_registro(lista, novo_registro, nome_modulo, chave_unica="codigo"):
    """
    Inclui um novo registro na lista com validação de duplicidade.
    
    Parâmetros:
        lista (list): Lista onde adicionar.
        novo_registro (dict): Novo registro a adicionar.
        nome_modulo (str): Nome do módulo (para salvar em arquivo).
        chave_unica (str): Campo que deve ser único.
    
    Retorna:
        bool: True se incluído com sucesso, False caso contrário.
    """
    if chave_unica in novo_registro:
        if codigo_existe(lista, novo_registro[chave_unica]):
            print(f"[AVISO] Código {novo_registro[chave_unica]} já existe.")
            return False
    
    lista.append(novo_registro)
    salvar_em_arquivo(nome_modulo, lista)
    return True

def listar_registros(lista, nome_modulo, campos_exibicao=None):
    """
    Lista todos os registros de um módulo.
    
    Parâmetros:
        lista (list): Lista de registros.
        nome_modulo (str): Nome do módulo.
        campos_exibicao (list): Campos a exibir (None = todos).
    """
    if not lista:
        print(f"\nNão há {nome_modulo} cadastrados.")
        return
    
    print(f"\nTotal de {nome_modulo} cadastrados: {len(lista)}\n")
    for i, registro in enumerate(lista, start=1):
        if campos_exibicao:
            valores = [str(registro.get(campo, "N/A")) for campo in campos_exibicao]
            print(f"  {i:>3}. {' | '.join(valores)}")
        else:
            print(f"  {i:>3}. {registro}")

def atualizar_registro(lista, codigo, dados_atualizados, nome_modulo):
    """
    Atualiza um registro existente.
    
    Parâmetros:
        lista (list): Lista de registros.
        codigo (int): Código do registro a atualizar.
        dados_atualizados (dict): Novos dados.
        nome_modulo (str): Nome do módulo.
    
    Retorna:
        bool: True se atualizado, False caso contrário.
    """
    registro = encontrar_por_codigo(lista, codigo)
    if registro:
        registro.update(dados_atualizados)
        salvar_em_arquivo(nome_modulo, lista)
        return True
    return False

def excluir_registro(lista, codigo, nome_modulo):
    """
    Exclui um registro da lista.
    
    Parâmetros:
        lista (list): Lista de registros.
        codigo (int): Código do registro a excluir.
        nome_modulo (str): Nome do módulo.
    
    Retorna:
        bool: True se excluído, False caso contrário.
    """
    for i, registro in enumerate(lista):
        if registro.get("codigo") == codigo:
            lista.pop(i)
            salvar_em_arquivo(nome_modulo, lista)
            return True
    return False

# ─────────────────────────────────────────────
# FUNÇÕES UTILITÁRIAS
# ─────────────────────────────────────────────

def limpar_tela():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(titulo):
    """Exibe um cabeçalho formatado."""
    print("\n" + "=" * 60)
    print(f"  {titulo.center(56)}")
    print("=" * 60)

def aguardar_enter():
    """Aguarda o usuário pressionar ENTER."""
    input("\nPressione ENTER para continuar.")

def validar_nome(nome, minimo=3, maximo=100):
    """Valida um nome."""
    if not nome or not nome.strip():
        return False, "O nome não pode estar vazio."
    if len(nome.strip()) < minimo:
        return False, f"O nome deve ter pelo menos {minimo} caracteres."
    if len(nome.strip()) > maximo:
        return False, f"O nome não pode ter mais de {maximo} caracteres."
    return True, "Válido"

def validar_cpf_basico(cpf):
    """Validação básica de CPF (apenas formato)."""
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
        return False, "CPF deve ter 11 dígitos (formato: XXX.XXX.XXX-XX)."
    return True, "Válido"

def solicitar_codigo_existente(lista, mensagem="Código"):
    """Solicita um código que deve existir na lista."""
    while True:
        try:
            codigo = int(input(f"\nDigite o {mensagem}: "))
            if encontrar_por_codigo(lista, codigo):
                return codigo
            else:
                print(f"[ERRO] {mensagem} {codigo} não encontrado.")
        except ValueError:
            print("[ERRO] Digite um número válido.")

# ─────────────────────────────────────────────
# FUNÇÕES DE ESTUDANTES
# ─────────────────────────────────────────────

def incluir_estudante():
    """Inclui um novo estudante."""
    exibir_cabecalho("INCLUSÃO DE ESTUDANTE")
    
    while True:
        try:
            nome = input("\nDigite o nome do estudante: ").strip()
            valido, mensagem = validar_nome(nome)
            if not valido:
                print(f"[ERRO] {mensagem}")
                continue
            
            codigo = gerar_proximo_codigo(estudantes)
            novo_estudante = {"codigo": codigo, "nome": nome}
            
            if incluir_registro(estudantes, novo_estudante, "estudantes"):
                print(f"[OK] Estudante '{nome}' incluído com sucesso (Código: {codigo}).")
                
                continuar = input("\nDeseja incluir outro estudante? (S/N): ").upper()
                while continuar not in ("S", "N"):
                    print("[ERRO] Digite 'S' ou 'N'.")
                    continuar = input("Deseja incluir outro estudante? (S/N): ").upper()
                
                if continuar == "N":
                    break
            else:
                print("[ERRO] Falha ao incluir estudante.")
                break
        except KeyboardInterrupt:
            print("\n\n[AVISO] Operação cancelada.")
            break
    
    aguardar_enter()

def listar_estudantes():
    """Lista todos os estudantes."""
    exibir_cabecalho("LISTAGEM DE ESTUDANTES")
    listar_registros(estudantes, "estudantes", ["codigo", "nome"])
    aguardar_enter()

def atualizar_estudante():
    """Atualiza um estudante existente."""
    exibir_cabecalho("ATUALIZAÇÃO DE ESTUDANTE")
    
    if not estudantes:
        print("\nNão há estudantes para atualizar.")
        aguardar_enter()
        return
    
    try:
        codigo = solicitar_codigo_existente(estudantes, "código do estudante")
        novo_nome = input("Digite o novo nome: ").strip()
        
        valido, mensagem = validar_nome(novo_nome)
        if not valido:
            print(f"[ERRO] {mensagem}")
            aguardar_enter()
            return
        
        if atualizar_registro(estudantes, codigo, {"nome": novo_nome}, "estudantes"):
            print(f"[OK] Estudante atualizado com sucesso.")
        else:
            print("[ERRO] Estudante não encontrado.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
    
    aguardar_enter()

def excluir_estudante():
    """Exclui um estudante."""
    exibir_cabecalho("EXCLUSÃO DE ESTUDANTE")
    
    if not estudantes:
        print("\nNão há estudantes para excluir.")
        aguardar_enter()
        return
    
    try:
        codigo = solicitar_codigo_existente(estudantes, "código do estudante")
        confirmacao = input(f"\nTem certeza que deseja excluir? (S/N): ").upper()
        
        if confirmacao == "S":
            if excluir_registro(estudantes, codigo, "estudantes"):
                print("[OK] Estudante excluído com sucesso.")
            else:
                print("[ERRO] Falha ao excluir.")
        else:
            print("[AVISO] Operação cancelada.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
    
    aguardar_enter()

def menu_estudantes():
    """Menu de operações de estudantes."""
    while True:
        exibir_cabecalho("ESTUDANTES - MENU DE OPERAÇÕES")
        print("\n  1. Incluir Estudante")
        print("  2. Listar Estudantes")
        print("  3. Atualizar Estudante")
        print("  4. Excluir Estudante")
        print("  0. Voltar ao Menu Principal")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            incluir_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "3":
            atualizar_estudante()
        elif opcao == "4":
            excluir_estudante()
        elif opcao == "0":
            break
        else:
            print("\n[ERRO] Opção inválida.")
            aguardar_enter()

# ─────────────────────────────────────────────
# FUNÇÕES DE PROFESSORES
# ─────────────────────────────────────────────

def incluir_professor():
    """Inclui um novo professor."""
    exibir_cabecalho("INCLUSÃO DE PROFESSOR")
    
    while True:
        try:
            nome = input("\nDigite o nome do professor: ").strip()
            valido, mensagem = validar_nome(nome)
            if not valido:
                print(f"[ERRO] {mensagem}")
                continue
            
            cpf = input("Digite o CPF (formato: XXX.XXX.XXX-XX): ").strip()
            valido, mensagem = validar_cpf_basico(cpf)
            if not valido:
                print(f"[ERRO] {mensagem}")
                continue
            
            codigo = gerar_proximo_codigo(professores)
            novo_professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
            
            if incluir_registro(professores, novo_professor, "professores"):
                print(f"[OK] Professor '{nome}' incluído com sucesso (Código: {codigo}).")
                
                continuar = input("\nDeseja incluir outro professor? (S/N): ").upper()
                while continuar not in ("S", "N"):
                    print("[ERRO] Digite 'S' ou 'N'.")
                    continuar = input("Deseja incluir outro professor? (S/N): ").upper()
                
                if continuar == "N":
                    break
            else:
                print("[ERRO] Falha ao incluir professor.")
                break
        except KeyboardInterrupt:
            print("\n\n[AVISO] Operação cancelada.")
            break
    
    aguardar_enter()

def listar_professores():
    """Lista todos os professores."""
    exibir_cabecalho("LISTAGEM DE PROFESSORES")
    listar_registros(professores, "professores", ["codigo", "nome", "cpf"])
    aguardar_enter()

def atualizar_professor():
    """Atualiza um professor."""
    exibir_cabecalho("ATUALIZAÇÃO DE PROFESSOR")
    
    if not professores:
        print("\nNão há professores para atualizar.")
        aguardar_enter()
        return
    
    try:
        codigo = solicitar_codigo_existente(professores, "código do professor")
        novo_nome = input("Digite o novo nome: ").strip()
        
        valido, mensagem = validar_nome(novo_nome)
        if not valido:
            print(f"[ERRO] {mensagem}")
            aguardar_enter()
            return
        
        novo_cpf = input("Digite o novo CPF: ").strip()
        valido, mensagem = validar_cpf_basico(novo_cpf)
        if not valido:
            print(f"[ERRO] {mensagem}")
            aguardar_enter()
            return
        
        if atualizar_registro(professores, codigo, {"nome": novo_nome, "cpf": novo_cpf}, "professores"):
            print("[OK] Professor atualizado com sucesso.")
        else:
            print("[ERRO] Professor não encontrado.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
    
    aguardar_enter()

def excluir_professor():
    """Exclui um professor."""
    exibir_cabecalho("EXCLUSÃO DE PROFESSOR")
    
    if not professores:
        print("\nNão há professores para excluir.")
        aguardar_enter()
        return
    
    try:
        codigo = solicitar_codigo_existente(professores, "código do professor")
        confirmacao = input(f"\nTem certeza que deseja excluir? (S/N): ").upper()
        
        if confirmacao == "S":
            if excluir_registro(professores, codigo, "professores"):
                print("[OK] Professor excluído com sucesso.")
            else:
                print("[ERRO] Falha ao excluir.")
        else:
            print("[AVISO] Operação cancelada.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
    
    aguardar_enter()

def menu_professores():
    """Menu de operações de professores."""
    while True:
        exibir_cabecalho("PROFESSORES - MENU DE OPERAÇÕES")
        print("\n  1. Incluir Professor")
        print("  2. Listar Professores")
        print("  3. Atualizar Professor")
        print("  4. Excluir Professor")
        print("  0. Voltar ao Menu Principal")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            incluir_professor()
        elif opcao == "2":
            listar_professores()
        elif opcao == "3":
            atualizar_professor()
        elif opcao == "4":
            excluir_professor()
        elif opcao == "0":
            break
        else:
            print("\n[ERRO] Opção inválida.")
            aguardar_enter()

# ─────────────────────────────────────────────
# FUNÇÕES DE DISCIPLINAS
# ─────────────────────────────────────────────

def incluir_disciplina():
    """Inclui uma nova disciplina."""
    exibir_cabecalho("INCLUSÃO DE DISCIPLINA")
    
    while True:
        try:
            nome = input("\nDigite o nome da disciplina: ").strip()
            valido, mensagem = validar_nome(nome)
            if not valido:
                print(f"[ERRO] {mensagem}")
                continue
            
            codigo = gerar_proximo_codigo(disciplinas)
            nova_disciplina = {"codigo": codigo, "nome": nome}
            
            if incluir_registro(disciplinas, nova_disciplina, "disciplinas"):
                print(f"[OK] Disciplina '{nome}' incluída com sucesso (Código: {codigo}).")
                
                continuar = input("\nDeseja incluir outra disciplina? (S/N): ").upper()
                while continuar not in ("S", "N"):
                    print("[ERRO] Digite 'S' ou 'N'.")
                    continuar = input("Deseja incluir outra disciplina? (S/N): ").upper()
                
                if continuar == "N":
                    break
            else:
                print("[ERRO] Falha ao incluir disciplina.")
                break
        except KeyboardInterrupt:
            print("\n\n[AVISO] Operação cancelada.")
            break
    
    aguardar_enter()

def listar_disciplinas():
    """Lista todas as disciplinas."""
    exibir_cabecalho("LISTAGEM DE DISCIPLINAS")
    listar_registros(disciplinas, "disciplinas", ["codigo", "nome"])
    aguardar_enter()

def atualizar_disciplina():
    """Atualiza uma disciplina."""
    exibir_cabecalho("ATUALIZAÇÃO DE DISCIPLINA")
    
    if not disciplinas:
        print("\nNão há disciplinas para atualizar.")
        aguardar_enter()
        return
    
    try:
        codigo = solicitar_codigo_existente(disciplinas, "código da disciplina")
        novo_nome = input("Digite o novo nome: ").strip()
        
        valido, mensagem = validar_nome(novo_nome)
        if not valido:
            print(f"[ERRO] {mensagem}")
            aguardar_enter()
            return
        
        if atualizar_registro(disciplinas, codigo, {"nome": novo_nome}, "disciplinas"):
            print("[OK] Disciplina atualizada com sucesso.")
        else:
            print("[ERRO] Disciplina não encontrada.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
    
    aguardar_enter()

def excluir_disciplina():
    """Exclui uma disciplina."""
    exibir_cabecalho("EXCLUSÃO DE DISCIPLINA")
    
    if not disciplinas:
        print("\nNão há disciplinas para excluir.")
        aguardar_enter()
        return
    
    try:
        codigo = solicitar_codigo_existente(disciplinas, "código da disciplina")
        confirmacao = input(f"\nTem certeza que deseja excluir? (S/N): ").upper()
        
        if confirmacao == "S":
            if excluir_registro(disciplinas, codigo, "disciplinas"):
                print("[OK] Disciplina excluída com sucesso.")
            else:
                print("[ERRO] Falha ao excluir.")
        else:
            print("[AVISO] Operação cancelada.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
    
    aguardar_enter()

def menu_disciplinas():
    """Menu de operações de disciplinas."""
    while True:
        exibir_cabecalho("DISCIPLINAS - MENU DE OPERAÇÕES")
        print("\n  1. Incluir Disciplina")
        print("  2. Listar Disciplinas")
        print("  3. Atualizar Disciplina")
        print("  4. Excluir Disciplina")
        print("  0. Voltar ao Menu Principal")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            incluir_disciplina()
        elif opcao == "2":
            listar_disciplinas()
        elif opcao == "3":
            atualizar_disciplina()
        elif opcao == "4":
            excluir_disciplina()
        elif opcao == "0":
            break
        else:
            print("\n[ERRO] Opção inválida.")
            aguardar_enter()

# ─────────────────────────────────────────────
# FUNÇÕES DE TURMAS
# ─────────────────────────────────────────────

def incluir_turma():
    """Inclui uma nova turma com validação de referências."""
    exibir_cabecalho("INCLUSÃO DE TURMA")
    
    if not professores:
        print("\n[ERRO] Não há professores cadastrados. Cadastre um professor primeiro.")
        aguardar_enter()
        return
    
    if not disciplinas:
        print("\n[ERRO] Não há disciplinas cadastradas. Cadastre uma disciplina primeiro.")
        aguardar_enter()
        return
    
    while True:
        try:
            codigo_professor = solicitar_codigo_existente(professores, "código do professor")
            if not encontrar_por_codigo(professores, codigo_professor):
                print("[ERRO] Professor não encontrado.")
                continue
            
            codigo_disciplina = solicitar_codigo_existente(disciplinas, "código da disciplina")
            if not encontrar_por_codigo(disciplinas, codigo_disciplina):
                print("[ERRO] Disciplina não encontrada.")
                continue
            
            codigo = gerar_proximo_codigo(turmas)
            nova_turma = {
                "codigo": codigo,
                "codigo_professor": codigo_professor,
                "codigo_disciplina": codigo_disciplina
            }
            
            if incluir_registro(turmas, nova_turma, "turmas"):
                print(f"[OK] Turma incluída com sucesso (Código: {codigo}).")
                
                continuar = input("\nDeseja incluir outra turma? (S/N): ").upper()
                while continuar not in ("S", "N"):
                    print("[ERRO] Digite 'S' ou 'N'.")
                    continuar = input("Deseja incluir outra turma? (S/N): ").upper()
                
                if continuar == "N":
                    break
            else:
                print("[ERRO] Falha ao incluir turma.")
                break
        except KeyboardInterrupt:
            print("\n\n[AVISO] Operação cancelada.")
            break
    
    aguardar_enter()

def listar_turmas():
    """Lista todas as turmas com informações de professor e disciplina."""
    exibir_cabecalho("LISTAGEM DE TURMAS")
    
    if not turmas:
        print("\nNão há turmas cadastradas.")
        aguardar_enter()
        return
    
    print(f"\nTotal de turmas cadastradas: {len(turmas)}\n")
    for i, turma in enumerate(turmas, start=1):
        prof = encontrar_por_codigo(professores, turma.get("codigo_professor", 0))
        disc = encontrar_por_codigo(disciplinas, turma.get("codigo_disciplina", 0))
        prof_nome = prof.get("nome", "N/A") if prof else "N/A"
        disc_nome = disc.get("nome", "N/A") if disc else "N/A"
        
        print(f"  {i:>3}. Turma {turma['codigo']} | Prof: {prof_nome} | Disc: {disc_nome}")
    
    aguardar_enter()

def atualizar_turma():
    """Atualiza uma turma."""
    exibir_cabecalho("ATUALIZAÇÃO DE TURMA")
    
    if not turmas:
        print("\nNão há turmas para atualizar.")
        aguardar_enter()
        return
    
    try:
        codigo = solicitar_codigo_existente(turmas, "código da turma")
        
        codigo_professor = solicitar_codigo_existente(professores, "código do novo professor")
        if not encontrar_por_codigo(professores, codigo_professor):
            print("[ERRO] Professor não encontrado.")
            aguardar_enter()
            return
        
        codigo_disciplina = solicitar_codigo_existente(disciplinas, "código da nova disciplina")
        if not encontrar_por_codigo(disciplinas, codigo_disciplina):
            print("[ERRO] Disciplina não encontrada.")
            aguardar_enter()
            return
        
        if atualizar_registro(turmas, codigo, {
            "codigo_professor": codigo_professor,
            "codigo_disciplina": codigo_disciplina
        }, "turmas"):
            print("[OK] Turma atualizada com sucesso.")
        else:
            print("[ERRO] Turma não encontrada.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
    
    aguardar_enter()

def excluir_turma():
    """Exclui uma turma."""
    exibir_cabecalho("EXCLUSÃO DE TURMA")
    
    if not turmas:
        print("\nNão há turmas para excluir.")
        aguardar_enter()
        return
    
    try:
        codigo = solicitar_codigo_existente(turmas, "código da turma")
        confirmacao = input(f"\nTem certeza que deseja excluir? (S/N): ").upper()
        
        if confirmacao == "S":
            if excluir_registro(turmas, codigo, "turmas"):
                print("[OK] Turma excluída com sucesso.")
            else:
                print("[ERRO] Falha ao excluir.")
        else:
            print("[AVISO] Operação cancelada.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
    
    aguardar_enter()

def menu_turmas():
    """Menu de operações de turmas."""
    while True:
        exibir_cabecalho("TURMAS - MENU DE OPERAÇÕES")
        print("\n  1. Incluir Turma")
        print("  2. Listar Turmas")
        print("  3. Atualizar Turma")
        print("  4. Excluir Turma")
        print("  0. Voltar ao Menu Principal")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            incluir_turma()
        elif opcao == "2":
            listar_turmas()
        elif opcao == "3":
            atualizar_turma()
        elif opcao == "4":
            excluir_turma()
        elif opcao == "0":
            break
        else:
            print("\n[ERRO] Opção inválida.")
            aguardar_enter()

# ─────────────────────────────────────────────
# FUNÇÕES DE MATRÍCULAS
# ─────────────────────────────────────────────

def incluir_matricula():
    """Inclui uma nova matrícula com validação de referências."""
    exibir_cabecalho("INCLUSÃO DE MATRÍCULA")
    
    if not turmas:
        print("\n[ERRO] Não há turmas cadastradas.")
        aguardar_enter()
        return
    
    if not estudantes:
        print("\n[ERRO] Não há estudantes cadastrados.")
        aguardar_enter()
        return
    
    while True:
        try:
            codigo_turma = solicitar_codigo_existente(turmas, "código da turma")
            if not encontrar_por_codigo(turmas, codigo_turma):
                print("[ERRO] Turma não encontrada.")
                continue
            
            codigo_estudante = solicitar_codigo_existente(estudantes, "código do estudante")
            if not encontrar_por_codigo(estudantes, codigo_estudante):
                print("[ERRO] Estudante não encontrado.")
                continue
            
            # Verificar se a matrícula já existe
            matricula_existe = any(
                m.get("codigo_turma") == codigo_turma and m.get("codigo_estudante") == codigo_estudante
                for m in matriculas
            )
            
            if matricula_existe:
                print("[AVISO] Este estudante já está matriculado nesta turma.")
                continuar = input("Deseja tentar outra matrícula? (S/N): ").upper()
                if continuar == "N":
                    break
                continue
            
            nova_matricula = {
                "codigo_turma": codigo_turma,
                "codigo_estudante": codigo_estudante
            }
            
            matriculas.append(nova_matricula)
            salvar_em_arquivo("matriculas", matriculas)
            print("[OK] Matrícula incluída com sucesso.")
            
            continuar = input("\nDeseja incluir outra matrícula? (S/N): ").upper()
            while continuar not in ("S", "N"):
                print("[ERRO] Digite 'S' ou 'N'.")
                continuar = input("Deseja incluir outra matrícula? (S/N): ").upper()
            
            if continuar == "N":
                break
        except KeyboardInterrupt:
            print("\n\n[AVISO] Operação cancelada.")
            break
    
    aguardar_enter()

def listar_matriculas():
    """Lista todas as matrículas."""
    exibir_cabecalho("LISTAGEM DE MATRÍCULAS")
    
    if not matriculas:
        print("\nNão há matrículas cadastradas.")
        aguardar_enter()
        return
    
    print(f"\nTotal de matrículas cadastradas: {len(matriculas)}\n")
    for i, matricula in enumerate(matriculas, start=1):
        turma = encontrar_por_codigo(turmas, matricula.get("codigo_turma", 0))
        estudante = encontrar_por_codigo(estudantes, matricula.get("codigo_estudante", 0))
        turma_info = f"Turma {turma['codigo']}" if turma else "Turma N/A"
        est_nome = estudante.get("nome", "N/A") if estudante else "N/A"
        
        print(f"  {i:>3}. {turma_info} | Estudante: {est_nome}")
    
    aguardar_enter()

def excluir_matricula():
    """Exclui uma matrícula."""
    exibir_cabecalho("EXCLUSÃO DE MATRÍCULA")
    
    if not matriculas:
        print("\nNão há matrículas para excluir.")
        aguardar_enter()
        return
    
    try:
        codigo_turma = int(input("\nDigite o código da turma: "))
        codigo_estudante = int(input("Digite o código do estudante: "))
        
        for i, matricula in enumerate(matriculas):
            if matricula.get("codigo_turma") == codigo_turma and matricula.get("codigo_estudante") == codigo_estudante:
                confirmacao = input(f"\nTem certeza que deseja excluir? (S/N): ").upper()
                if confirmacao == "S":
                    matriculas.pop(i)
                    salvar_em_arquivo("matriculas", matriculas)
                    print("[OK] Matrícula excluída com sucesso.")
                else:
                    print("[AVISO] Operação cancelada.")
                aguardar_enter()
                return
        
        print("[ERRO] Matrícula não encontrada.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
    
    aguardar_enter()

def menu_matriculas():
    """Menu de operações de matrículas."""
    while True:
        exibir_cabecalho("MATRÍCULAS - MENU DE OPERAÇÕES")
        print("\n  1. Incluir Matrícula")
        print("  2. Listar Matrículas")
        print("  3. Excluir Matrícula")
        print("  0. Voltar ao Menu Principal")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            incluir_matricula()
        elif opcao == "2":
            listar_matriculas()
        elif opcao == "3":
            excluir_matricula()
        elif opcao == "0":
            break
        else:
            print("\n[ERRO] Opção inválida.")
            aguardar_enter()

# ─────────────────────────────────────────────
# MENU PRINCIPAL
# ─────────────────────────────────────────────

def menu_principal():
    """Menu principal do sistema."""
    while True:
        try:
            exibir_cabecalho("SISTEMA DE GESTÃO ACADÊMICA")
            print("\n  1. Estudantes")
            print("  2. Professores")
            print("  3. Disciplinas")
            print("  4. Turmas")
            print("  5. Matrículas")
            print("  0. Sair")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                menu_estudantes()
            elif opcao == "2":
                menu_professores()
            elif opcao == "3":
                menu_disciplinas()
            elif opcao == "4":
                menu_turmas()
            elif opcao == "5":
                menu_matriculas()
            elif opcao == "0":
                print("\nSaindo do sistema. Até logo!")
                break
            else:
                print("\n[ERRO] Opção inválida.")
                aguardar_enter()
        except EOFError:
            break

# ─────────────────────────────────────────────
# PONTO DE ENTRADA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    try:
        carregar_todos_dados()
        menu_principal()
    except EOFError:
        pass
