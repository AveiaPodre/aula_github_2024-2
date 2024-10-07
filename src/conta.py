import random
import string

class Conta:
    def __init__(self, cliente, saldo=0):
        self.codigo = self.gerar_codigo_conta()
        self.cliente = cliente
        self.saldo = saldo
        self.transacoes = []

    def gerar_codigo_conta(self, length=8):
        caracteres = string.ascii_uppercase + string.digits
        return ''.join(random.choice(caracteres) for _ in range(length))

    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.log_transacao("depósito", valor)
            return 'Depósito realizado com sucesso'
        else:
            return 'Valor inválido para depósito'
     
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.log_transacao("saque", valor)
            return "Saque realizado com sucesso"
        else:
            return "Saldo insuficiente"
    
    def transferir(self, conta_destino, valor):
        if self.sacar(valor) == "Saque realizado com sucesso":
            return conta_destino.depositar(valor)
        else:
            return "Transferência falhou"
    
    def log_transacao(self, tipo, valor):
        self.transacoes.append({'tipo': tipo, 'valor': valor, 'saldo': self.saldo})