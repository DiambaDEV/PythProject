class Pacientes:
    def __init__(self, nome, cpf, telefone, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf} - Tel: {self.telefone} - Nasc: {self.data_nascimento}"
    