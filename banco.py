class Banco (object):
    def __init__(self):
        #TODO: Implementar
    
    def inserir_cliente(self, cliente):
        #TODO: Implementar
    
    def inserir_conta(self, conta):
        #TODO: Implementar
    
    def autenticar(self, cliente):
        #TODO: Implementar
    
    def deposito(self, conta, valor):
        if conta in self.contas:
            conta.depositar(valor)
            print('Depósito realizado com sucesso')
        else:
            print('Conta não encontrada')
    
    def saque(self, conta, valor):
        #TODO: Implementar
    
    def transferencia(self, conta_origem, conta_destino, valor):
        #TODO: Implementar
    
    def saldo(self, conta):
        #TODO: Implementar