class Conta:
    def init(self, cpf, titular, saldo=0):
        self.cpf = cpf
        self.titular = titular
        self.saldo = saldo
        
    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print('Depósito realizado com sucesso')
        else:
            print('Valor inválido para depósito')
        
    def sacar(self, valor):
        #Todo: Implementar
        return
    
    def transferir(self, conta_destino, valor):
        #Todo: Implementar
        return
    
    
    
    