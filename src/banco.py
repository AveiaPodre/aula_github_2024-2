from cliente import Cliente
from conta import Conta

class Banco(object):
    def __init__(self):
        self.clientes = []
    
    def inserir_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            return "Cliente deve ser uma instância da classe Cliente."

        if self.autenticar_cliente(cliente):
            return "Cliente já existe."
        
        self.clientes.append(cliente)
        return "Cliente inserido com sucesso."
    
    def criar_conta(self, cliente, saldo=0):
        if not isinstance(cliente, Cliente):
            return "Cliente deve ser uma instância da classe Cliente."

        if not self.autenticar_cliente(cliente):
            return "Cliente não encontrado."

        conta = Conta(cliente, saldo)
        cliente.adicionar_conta(conta)
        return conta
    
    def autenticar_cliente(self, cliente):
        return cliente in self.clientes
    
    def deposito(self, codigo_conta, valor):
        conta = self.procurar_conta_por_codigo(codigo_conta)
        if conta:
            return conta.depositar(valor)
        else:
            return 'Conta não encontrada'
    
    def saque(self, codigo_conta, valor):
        conta = self.procurar_conta_por_codigo(codigo_conta)
        if conta:
            return conta.sacar(valor)
        else:
            return 'Conta não encontrada'
    
    def transferencia(self, cliente_origem, conta_origem, cliente_destino, conta_destino, valor):
        if self.autenticar_cliente(cliente_origem) and conta_origem in cliente_origem.contas and \
           self.autenticar_cliente(cliente_destino) and conta_destino in cliente_destino.contas:
            return conta_origem.transferir(conta_destino, valor)
        else:
            return 'Conta ou cliente não encontrado'
    
    def saldo(self, cliente, conta):
        if self.autenticar_cliente(cliente) and conta in cliente.contas:
            return conta.consultar_saldo()
        else:
            return 'Conta ou cliente não encontrado'
    
    def procurar_conta_por_codigo(self, codigo):
        for cliente in self.clientes:
            for conta in cliente.contas:
                if conta.codigo == codigo:
                    return conta
        return None