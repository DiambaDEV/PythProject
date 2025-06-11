from pessoas import Pacientes

class BancoDeDados:
    def __init__(self):
        self.pacientes = []

    def adicionar(self, paciente):
        self.pacientes.append(paciente)

    def listar(self):
        return self.pacientes
    
    def buscar_por_cpf(self, cpf):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None
        
    def remover(self, cpf):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                self.pacientes.remove(paciente)
                return True
        return False

    def editar(self, cpf, novo_nome=None, novo_telefone=None, nova_data=None):
        paciente = self.buscar_por_cpf(cpf)
        if paciente:
            if novo_nome:
                paciente.nome = novo_nome
            if novo_telefone:
                paciente.telefone = novo_telefone
            if nova_data:
                paciente.data_nascimento = nova_data
            return True
        return False
    
