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
        

    
