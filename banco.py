class Banco (object):
    def __init__(self):
        #TODO: Implementar
    
    def inserir_cliente(self, cliente):
        #TODO: Implementar
    
    def inserir_conta(self, conta):
        #TODO: Implementar
    
    def autenticar(self, cliente):
        for c in self.clientes:
            if c.nome == cliente.nome:
                return True
        return False
    
    def deposito(self, conta, valor):
        #TODO: Implementar
    
    def saque(self, conta, valor):
        #TODO: Implementar
    
    def transferencia(self, conta_origem, conta_destino, valor):
        #TODO: Implementar
    
    def saldo(self, conta):
        #TODO: Implementar