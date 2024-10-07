from conta import Conta 

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        if isinstance(conta, Conta):
            self.contas.append(conta)
            return "Conta adicionada com sucesso."
        else:
            return "Conta inválida."

    def listar_contas(self):
        return self.contas