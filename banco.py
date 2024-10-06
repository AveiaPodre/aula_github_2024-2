import re

class Banco(object):
    def __init__(self):
        self.clientes = []
        self.contas = []
    
    def inserir_cliente(self, cliente):
        if cliente in self.clientes:
            print("Cliente já existe.")
            return
        
        self.clientes.append(cliente)
        print("Cliente inserido com sucesso.")
        return
    
    def inserir_conta(self):
        cpf = input("Digite o CPF do titular (somente números): ")
        if not re.match(r'^\d{11}$', cpf):
            print("CPF inválido. Deve conter exatamente 11 dígitos.")
            return

        nome = input("Digite o nome do titular: ")
        if not re.match(r'^[A-Za-z\s]+$', nome):
            print("Nome inválido. Deve conter apenas letras e espaços.")
            return

        try:
            saldo_inicial = float(input("Digite o saldo inicial: "))
        except ValueError:
            print("Saldo inicial inválido. Deve ser um número.")
            return

        conta = {
            'cpf': cpf,
            'nome': nome,
            'saldo': saldo_inicial
        }

        self.contas.add(conta)
        return
    
    def autenticar(self, cliente):
        for c in self.clientes:
            if c.nome == cliente.nome:
                return True
        return False
    
    def deposito(self, conta, valor):
        if conta in self.contas:
            conta.depositar(valor)
            print('Depósito realizado com sucesso')
        else:
            print('Conta não encontrada')
    
    def saque(self, conta, valor):
        #TODO: Implementar
        return
    
    def transferencia(self, conta_origem, conta_destino, valor):
        #TODO: Implementar
        return
    
    def saldo(self, conta):
        return conta.consultar_saldo()