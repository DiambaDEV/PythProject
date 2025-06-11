from pessoas.Pacientes import Pacientes
from repositorio.BancoDeDados import BancoDeDados
import sys
import os
import re
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def validar_cpf(cpf):
    import re
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, cpf))


def pedir_cpf():
    while True:
        cpf = input("CPF (formato: 000.000.000-00): ")
        if validar_cpf(cpf):
            return cpf
        print("CPF inválido. Use o formato 000.000.000-00.")

def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%y")
        return True
    except ValueError:
        return False

def pedir_data_nascimento():
    while True:
        nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        try:
            data = datetime.strptime(nascimento, "%d/%m/%Y")
            return data.strftime("%d/%m/%Y")  # Retorna como string formatada
        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA.")

def pedir_telefone():
    while True:
        telefone = input("Telefone (formato: (XX) XXXXX-XXXX): ")
        if re.match(r"^\(\d{2}\) \d{5}-\d{4}$", telefone):
            return telefone
        print("Formato inválido. Use: (XX) XXXXX-XXXX")

def menu():
    print("\n1. Cadastrar paciente")
    print("2. Listar pacientes")
    print("3. Buscar paciente por CPF")
    print("4. Editar paciente")
    print("5. Remover paciente")
    print("6. Sair")

repo = BancoDeDados()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        cpf = pedir_cpf()
        telefone = pedir_telefone()
        nascimento = pedir_data_nascimento()

        paciente = Pacientes(nome, cpf, telefone, nascimento)
        repo.adicionar(paciente)
        print("Paciente cadastrado com sucesso!")

    elif opcao == "2":
        print("\n Lista de pacientes:")
        for p in repo.listar():
            print(p)

    elif opcao == "3":
        cpf = pedir_cpf()
        paciente = repo.buscar_por_cpf(cpf)
        if paciente:
            print("Encontrado:", paciente)
        else:
            print("Paciente não encontrado.")

    elif opcao == "4":
        cpf = pedir_cpf()
        paciente = repo.buscar_por_cpf(cpf)
        if not paciente:
            print("Paciente não encontrado.")
        else:
            print("Deixe em branco para manter os dados atuais.")
            nome = input(f"Novo nome ({paciente.nome}): ") or None
            telefone = input(f"Novo telefone ({paciente.telefone}): ") or None
            nascimento = input(f"Nova data de nascimento ({paciente.data_nascimento}): ") or None
            if nascimento and not validar_data(nascimento):
                print("Data inválida. Edição cancelada.")
            else:
                repo.editar(cpf, nome, telefone, nascimento)
                print(" Dados atualizados com sucesso!")

    elif opcao == "5":
        cpf = pedir_cpf()
        if repo.remover(cpf):
            print("Paciente removido com sucesso!")
        else:
            print("Paciente não encontrado.")
        

    elif opcao == "6":
        print("Saindo.")
        break

    else:
        print("Opção inválida. Tente novamente.")
