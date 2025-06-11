from pessoas.Pacientes import Pacientes
from repositorio.BancoDeDados import BancoDeDados

def menu():
    print("\n1. Cadastrar paciente")
    print("2. Listar pacientes")
    print("3. Buscar paciente por CPF")
    print("4. Sair")

repo = BancoDeDados()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        paciente = Pacientes(nome, cpf, telefone, nascimento)
        repo.adicionar(paciente)
        print("Paciente cadastrado com sucesso!")

    elif opcao == "2":
        for p in repo.listar():
            print(p)

    elif opcao == "3":
        cpf = input("Digite o CPF: ")
        paciente = repo.buscar_por_cpf(cpf)
        if paciente:
            print("Encontrado:", paciente)
        else:
            print("Paciente não encontrado.")

    elif opcao == "4":
        print("Saindo.")
        break

    else:
        print("Opção inválida.")
