class Conta:
    def init(self, cpf, titular, saldo=0):
        self.cpf = cpf
        self.titular = titular
        self.saldo = saldo
        
    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self, valor):
        #Todo: Implementar]
        return
        
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
    
    def transferir(self, conta_destino, valor):
        #Todo: Implementar
        return
    
    
    
    