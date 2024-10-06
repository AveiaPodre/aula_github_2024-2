class Conta:

    def init(self, cpf, titular, saldo=0):
        self.cpf = cpf
        self.titular = titular
        self.saldo = saldo
        self.transacoes = []
        
    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.log_transacao("depósito", valor)
            print('Depósito realizado com sucesso')
        else:
            print('Valor inválido para depósito')
     
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.log_transacao("saque", valor)
            return True
        else:
            return False
    
    def transferir(self, conta_destino, valor):
        #Todo: Implementar
        return
    
    def log_transacao(self, tipo, valor):
        self.transacoes.append({'tipo': tipo, 'valor': valor, 'saldo': self.saldo})
    
    
    
    