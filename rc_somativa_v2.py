# Nome: ANDRÉ TEIXEIRA
# Curso: INTELIGENCIA ARTIFICIAL APLICADA
# Atividade: CRUD COMPLETO - RACIOCÍNIO COMPUTACIONAL
# Versão: 2.1 - Parte 2 (Finalizada e Corrigida)
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
    """Salva dados em arquivo JSON."""
    try:
        arquivo = ARQUIVOS.get(nome_modulo)
        if arquivo:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[ERRO] Falha ao salvar dados: {str(e)}")

def carregar_de_arquivo(nome_modulo):
    """Carrega dados de arquivo JSON."""
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
    """Gera o próximo código automático baseado no maior código existente."""
    if not lista:
        return 1
    return max(reg.get("codigo", 0) for reg in lista) + 1

def codigo_existe(lista, codigo):
    """Verifica se um código já existe na lista."""
    return any(reg.get("codigo") == codigo for reg in lista)

def encontrar_por_codigo(lista, codigo):
    """Encontra um registro pelo código."""
    for reg in lista:
        if reg.get("codigo") == codigo:
            return reg
    return None

def incluir_registro(lista, novo_registro, nome_modulo, chave_unica="codigo"):
    """Inclui um novo registro na lista com validação de duplicidade."""
    if chave_unica in novo_registro:
        if codigo_existe(lista, novo_registro[chave_unica]):
            print(f"[AVISO] Código {novo_registro[chave_unica]} já existe.")
            return False
    
    lista.append(novo_registro)
    salvar_em_arquivo(nome_modulo, lista)
    return True

def listar_registros(lista, nome_modulo, campos_exibicao=None):
    """Lista todos os registros de um módulo."""
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
    """Atualiza um registro existente."""
    registro = encontrar_por_codigo(lista, codigo)
    if registro:
        registro.update(dados_atualizados)
        salvar_em_arquivo(nome_modulo, lista)
        return True
    return False

def excluir_registro(lista, codigo, nome_modulo):
    """Exclui um registro da lista."""
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
# FUNÇÕES DE ESTUDANTES (CORRIGIDA)
# ─────────────────────────────────────────────

def incluir_estudante():
    """Inclui um novo estudante com tratamento de erro corrigido."""
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
                if continuar == "N":
                    break
        except KeyboardInterrupt:
            print("\n\n[AVISO] Operação cancelada.")
            break
    
    aguardar_enter()

def listar_estudantes():
    exibir_cabecalho("LISTAGEM DE ESTUDANTES")
    listar_registros(estudantes, "estudantes", ["codigo", "nome"])
    aguardar_enter()

def atualizar_estudante():
    exibir_cabecalho("ATUALIZAÇÃO DE ESTUDANTE")
    if not estudantes:
        print("\nNão há estudantes cadastrados."); aguardar_enter(); return
    try:
        codigo = solicitar_codigo_existente(estudantes, "código do estudante")
        novo_nome = input("Digite o novo nome: ").strip()
        valido, mensagem = validar_nome(novo_nome)
        if valido and atualizar_registro(estudantes, codigo, {"nome": novo_nome}, "estudantes"):
            print("[OK] Estudante atualizado com sucesso.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
    aguardar_enter()

def excluir_estudante():
    exibir_cabecalho("EXCLUSÃO DE ESTUDANTE")
    if not estudantes:
        print("\nNão há estudantes cadastrados."); aguardar_enter(); return
    codigo = solicitar_codigo_existente(estudantes, "código do estudante")
    if input("\nTem certeza que deseja excluir? (S/N): ").upper() == "S":
        excluir_registro(estudantes, codigo, "estudantes")
        print("[OK] Estudante excluído.")
    aguardar_enter()

def menu_estudantes():
    while True:
        exibir_cabecalho("ESTUDANTES - MENU DE OPERAÇÕES")
        print("\n  1. Incluir\n  2. Listar\n  3. Atualizar\n  4. Excluir\n  0. Voltar")
        op = input("\nEscolha: ")
        if op == "1": incluir_estudante()
        elif op == "2": listar_estudantes()
        elif op == "3": atualizar_estudante()
        elif op == "4": excluir_estudante()
        elif op == "0": break

# ─────────────────────────────────────────────
# FUNÇÕES DE PROFESSORES
# ─────────────────────────────────────────────

def incluir_professor():
    exibir_cabecalho("INCLUSÃO DE PROFESSOR")
    while True:
        try:
            nome = input("\nNome: ").strip()
            cpf = input("CPF (XXX.XXX.XXX-XX): ").strip()
            if validar_nome(nome)[0] and validar_cpf_basico(cpf)[0]:
                codigo = gerar_proximo_codigo(professores)
                if incluir_registro(professores, {"codigo": codigo, "nome": nome, "cpf": cpf}, "professores"):
                    print(f"[OK] Incluído (Código: {codigo}).")
                    if input("\nOutro? (S/N): ").upper() == "N": break
        except KeyboardInterrupt: break
    aguardar_enter()

def listar_professores():
    exibir_cabecalho("LISTAGEM DE PROFESSORES")
    listar_registros(professores, "professores", ["codigo", "nome", "cpf"])
    aguardar_enter()

def atualizar_professor():
    exibir_cabecalho("ATUALIZAÇÃO DE PROFESSOR")
    if not professores: print("\nVazio."); aguardar_enter(); return
    codigo = solicitar_codigo_existente(professores, "código")
    nome = input("Novo nome: ").strip()
    cpf = input("Novo CPF: ").strip()
    if atualizar_registro(professores, codigo, {"nome": nome, "cpf": cpf}, "professores"):
        print("[OK] Atualizado.")
    aguardar_enter()

def excluir_professor():
    exibir_cabecalho("EXCLUSÃO DE PROFESSOR")
    if not professores: print("\nVazio."); aguardar_enter(); return
    codigo = solicitar_codigo_existente(professores, "código")
    if input("Confirmar? (S/N): ").upper() == "S":
        excluir_registro(professores, codigo, "professores")
        print("[OK] Excluído.")
    aguardar_enter()

def menu_professores():
    while True:
        exibir_cabecalho("PROFESSORES - MENU")
        print("\n  1. Incluir\n  2. Listar\n  3. Atualizar\n  4. Excluir\n  0. Voltar")
        op = input("\nEscolha: ")
        if op == "1": incluir_professor()
        elif op == "2": listar_professores()
        elif op == "3": atualizar_professor()
        elif op == "4": excluir_professor()
        elif op == "0": break

# ─────────────────────────────────────────────
# FUNÇÕES DE DISCIPLINAS
# ─────────────────────────────────────────────

def incluir_disciplina():
    exibir_cabecalho("INCLUSÃO DE DISCIPLINA")
    while True:
        nome = input("\nNome da disciplina: ").strip()
        if validar_nome(nome)[0]:
            codigo = gerar_proximo_codigo(disciplinas)
            incluir_registro(disciplinas, {"codigo": codigo, "nome": nome}, "disciplinas")
            print(f"[OK] Incluída (Código: {codigo}).")
            if input("\nOutra? (S/N): ").upper() == "N": break
    aguardar_enter()

def listar_disciplinas():
    exibir_cabecalho("LISTAGEM DE DISCIPLINAS")
    listar_registros(disciplinas, "disciplinas", ["codigo", "nome"])
    aguardar_enter()

def atualizar_disciplina():
    exibir_cabecalho("ATUALIZAÇÃO DE DISCIPLINA")
    codigo = solicitar_codigo_existente(disciplinas, "código")
    nome = input("Novo nome: ").strip()
    if atualizar_registro(disciplinas, codigo, {"nome": nome}, "disciplinas"):
        print("[OK] Atualizado.")
    aguardar_enter()

def excluir_disciplina():
    exibir_cabecalho("EXCLUSÃO DE DISCIPLINA")
    codigo = solicitar_codigo_existente(disciplinas, "código")
    if input("Confirmar? (S/N): ").upper() == "S":
        excluir_registro(disciplinas, codigo, "disciplinas")
        print("[OK] Excluído.")
    aguardar_enter()

def menu_disciplinas():
    while True:
        exibir_cabecalho("DISCIPLINAS - MENU")
        print("\n  1. Incluir\n  2. Listar\n  3. Atualizar\n  4. Excluir\n  0. Voltar")
        op = input("\nEscolha: ")
        if op == "1": incluir_disciplina()
        elif op == "2": listar_disciplinas()
        elif op == "3": atualizar_disciplina()
        elif op == "4": excluir_disciplina()
        elif op == "0": break

# ─────────────────────────────────────────────
# FUNÇÕES DE TURMAS
# ─────────────────────────────────────────────

def incluir_turma():
    exibir_cabecalho("INCLUSÃO DE TURMA")
    if not professores or not disciplinas:
        print("[ERRO] Cadastre professor e disciplina primeiro."); aguardar_enter(); return
    cp = solicitar_codigo_existente(professores, "cód. professor")
    cd = solicitar_codigo_existente(disciplinas, "cód. disciplina")
    codigo = gerar_proximo_codigo(turmas)
    incluir_registro(turmas, {"codigo": codigo, "codigo_professor": cp, "codigo_disciplina": cd}, "turmas")
    print(f"[OK] Turma {codigo} criada."); aguardar_enter()

def listar_turmas():
    exibir_cabecalho("LISTAGEM DE TURMAS")
    if not turmas: print("\nVazio."); aguardar_enter(); return
    for t in turmas:
        p = encontrar_por_codigo(professores, t['codigo_professor'])
        d = encontrar_por_codigo(disciplinas, t['codigo_disciplina'])
        print(f"Turma {t['codigo']} | Prof: {p['nome'] if p else 'N/A'} | Disc: {d['nome'] if d else 'N/A'}")
    aguardar_enter()

def atualizar_turma():
    exibir_cabecalho("ATUALIZAÇÃO DE TURMA")
    codigo = solicitar_codigo_existente(turmas, "código da turma")
    cp = solicitar_codigo_existente(professores, "novo cód. professor")
    cd = solicitar_codigo_existente(disciplinas, "novo cód. disciplina")
    if atualizar_registro(turmas, codigo, {"codigo_professor": cp, "codigo_disciplina": cd}, "turmas"):
        print("[OK] Turma atualizada.")
    aguardar_enter()

def excluir_turma():
    exibir_cabecalho("EXCLUSÃO DE TURMA")
    codigo = solicitar_codigo_existente(turmas, "código")
    if input("Confirmar? (S/N): ").upper() == "S":
        excluir_registro(turmas, codigo, "turmas")
        print("[OK] Excluída.")
    aguardar_enter()

def menu_turmas():
    while True:
        exibir_cabecalho("TURMAS - MENU")
        print("\n  1. Incluir\n  2. Listar\n  3. Atualizar\n  4. Excluir\n  0. Voltar")
        op = input("\nEscolha: ")
        if op == "1": incluir_turma()
        elif op == "2": listar_turmas()
        elif op == "3": atualizar_turma()
        elif op == "4": excluir_turma()
        elif op == "0": break

# ─────────────────────────────────────────────
# FUNÇÕES DE MATRÍCULAS (CRUD COMPLETO FINALIZADO)
# ─────────────────────────────────────────────

def incluir_matricula():
    exibir_cabecalho("INCLUSÃO DE MATRÍCULA")
    if not turmas or not estudantes:
        print("[ERRO] Cadastre turma e estudante primeiro."); aguardar_enter(); return
    ct = solicitar_codigo_existente(turmas, "cód. turma")
    ce = solicitar_codigo_existente(estudantes, "cód. estudante")
    if any(m['codigo_turma'] == ct and m['codigo_estudante'] == ce for m in matriculas):
        print("[AVISO] Matrícula já existe."); aguardar_enter(); return
    matriculas.append({"codigo_turma": ct, "codigo_estudante": ce})
    salvar_em_arquivo("matriculas", matriculas)
    print("[OK] Matrícula realizada."); aguardar_enter()

def listar_matriculas():
    exibir_cabecalho("LISTAGEM DE MATRÍCULAS")
    if not matriculas: print("\nVazio."); aguardar_enter(); return
    for m in matriculas:
        e = encontrar_por_codigo(estudantes, m['codigo_estudante'])
        print(f"Turma {m['codigo_turma']} | Estudante: {e['nome'] if e else 'N/A'}")
    aguardar_enter()

def atualizar_matricula():
    """Atualiza uma matrícula existente."""
    exibir_cabecalho("ATUALIZAÇÃO DE MATRÍCULA")
    if not matriculas:
        print("\nNão há matrículas."); aguardar_enter(); return
    try:
        print("\nInforme os dados atuais:")
        ct_at = int(input("Cód. Turma: "))
        ce_at = int(input("Cód. Estudante: "))
        
        idx = -1
        for i, m in enumerate(matriculas):
            if m['codigo_turma'] == ct_at and m['codigo_estudante'] == ce_at:
                idx = i; break
        
        if idx == -1:
            print("[ERRO] Não encontrada."); aguardar_enter(); return

        print("\n--- Novos dados ---")
        ct_nv = solicitar_codigo_existente(turmas, "nova turma")
        ce_nv = solicitar_codigo_existente(estudantes, "novo estudante")
        
        if any(m['codigo_turma'] == ct_nv and m['codigo_estudante'] == ce_nv for m in matriculas):
            print("[AVISO] Já existe essa matrícula.")
        else:
            matriculas[idx] = {"codigo_turma": ct_nv, "codigo_estudante": ce_nv}
            salvar_em_arquivo("matriculas", matriculas)
            print("[OK] Atualizada.")
    except ValueError: print("[ERRO] Apenas números.")
    aguardar_enter()

def excluir_matricula():
    exibir_cabecalho("EXCLUSÃO DE MATRÍCULA")
    try:
        ct = int(input("Cód. Turma: "))
        ce = int(input("Cód. Estudante: "))
        for i, m in enumerate(matriculas):
            if m['codigo_turma'] == ct and m['codigo_estudante'] == ce:
                if input("Excluir? (S/N): ").upper() == "S":
                    matriculas.pop(i); salvar_em_arquivo("matriculas", matriculas)
                    print("[OK] Removida."); aguardar_enter(); return
        print("[ERRO] Não encontrada.")
    except ValueError: print("[ERRO] Inválido.")
    aguardar_enter()

def menu_matriculas():
    while True:
        exibir_cabecalho("MATRÍCULAS - MENU")
        print("\n  1. Incluir\n  2. Listar\n  3. Atualizar\n  4. Excluir\n  0. Voltar")
        op = input("\nEscolha: ")
        if op == "1": incluir_matricula()
        elif op == "2": listar_matriculas()
        elif op == "3": atualizar_matricula()
        elif op == "4": excluir_matricula()
        elif op == "0": break

# ─────────────────────────────────────────────
# MENU PRINCIPAL
# ─────────────────────────────────────────────

def menu_principal():
    while True:
        try:
            exibir_cabecalho("SISTEMA DE GESTÃO ACADÊMICA")
            print("\n  1. Estudantes\n  2. Professores\n  3. Disciplinas\n  4. Turmas\n  5. Matrículas\n  0. Sair")
            op = input("\nEscolha uma opção: ")
            if op == "1": menu_estudantes()
            elif op == "2": menu_professores()
            elif op == "3": menu_disciplinas()
            elif op == "4": menu_turmas()
            elif op == "5": menu_matriculas()
            elif op == "0": print("\nSaindo do sistema. Até logo!"); break
            else: print("[ERRO] Opção inválida."); aguardar_enter()
        except EOFError: break

# ─────────────────────────────────────────────
# PONTO DE ENTRADA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    carregar_todos_dados()
    menu_principal()