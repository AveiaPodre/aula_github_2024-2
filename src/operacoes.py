from banco import Banco
from conta import Conta
from cliente import Cliente

def criar_cliente(banco):
    nome = input("Informe o nome do cliente: ")
    cpf = input("Informe o CPF do cliente: ")
    cliente = Cliente(nome, cpf)
    print(banco.inserir_cliente(cliente))

def criar_conta(banco):
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in banco.clientes if c.cpf == cpf), None)
    if cliente:
        saldo = float(input("Informe o saldo inicial da conta: "))
        resultado = banco.criar_conta(cliente, saldo)
        if isinstance(resultado, Conta):
            print(f"Conta criada com sucesso. Código da conta: {resultado.codigo}")
        else:
            print(resultado)
    else:
        print("Cliente não encontrado.")

def realizar_deposito(banco):
    codigo_conta = input("Informe o código da conta: ")
    valor = float(input("Informe o valor do depósito: "))
    print(banco.deposito(codigo_conta, valor))

def realizar_saque(banco):
    codigo_conta = input("Informe o código da conta: ")
    valor = float(input("Informe o valor do saque: "))
    print(banco.saque(codigo_conta, valor))

def realizar_transferencia(banco):
    cpf_origem = input("Informe o CPF do cliente de origem: ")
    cliente_origem = next((c for c in banco.clientes if c.cpf == cpf_origem), None)
    if not cliente_origem:
        print("Cliente de origem não encontrado.")
        return

    codigo_conta_origem = input("Informe o código da conta de origem: ")
    conta_origem = banco.procurar_conta_por_codigo(codigo_conta_origem)
    if not conta_origem:
        print("Conta de origem não encontrada.")
        return

    cpf_destino = input("Informe o CPF do cliente de destino: ")
    cliente_destino = next((c for c in banco.clientes if c.cpf == cpf_destino), None)
    if not cliente_destino:
        print("Cliente de destino não encontrado.")
        return

    codigo_conta_destino = input("Informe o código da conta de destino: ")
    conta_destino = banco.procurar_conta_por_codigo(codigo_conta_destino)
    if not conta_destino:
        print("Conta de destino não encontrada.")
        return

    valor = float(input("Informe o valor da transferência: "))
    print(banco.transferencia(cliente_origem, conta_origem, cliente_destino, conta_destino, valor))

def consultar_saldo(banco):
    codigo_conta = input("Informe o código da conta: ")
    conta = banco.procurar_conta_por_codigo(codigo_conta)
    if conta:
        print(f"Saldo: {conta.consultar_saldo()}")
    else:
        print("Conta não encontrada.")

def listar_clientes(banco):
    if banco.clientes:
        for cliente in banco.clientes:
            print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}")
    else:
        print("Nenhum cliente cadastrado.")

def listar_contas_cliente(banco):
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in banco.clientes if c.cpf == cpf), None)
    if cliente:
        if cliente.contas:
            for conta in cliente.contas:
                print(f"Código da Conta: {conta.codigo}, Saldo: {conta.saldo}")
        else:
            print("Nenhuma conta cadastrada para este cliente.")
    else:
        print("Cliente não encontrado.")