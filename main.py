from menu import Menu
from banco import Banco
from conta import Conta

if __name__ == "__main__":
    banco = Banco()

    main_menu = Menu(["Criar Conta", "Saldo", "Depositar", "Sacar", "Ver Relatório de Transações", "Sair"], "Menu Principal")
    while True:
        op = main_menu.get_selection()
        if op == 1:
            print("Criar Conta foi selecionada")
            banco.inserir_conta()
        elif op == 2:
            print("Saldo foi selecionada")
            conta_numero = input("Digite o número da conta: ")
            conta = banco.buscar_conta(conta_numero)
            if conta:
                print(f"Saldo da conta {conta_numero}: {conta.consultar_saldo()}")
            else:
                print("Conta não encontrada")
        elif op == 3:
            print("Depositar foi selecionada")
            conta_numero = input("Digite o número da conta: ")
            conta = banco.buscar_conta(conta_numero)
            if conta:
                valor = float(input("Digite o valor a ser depositado: "))
                conta.depositar(valor)
                print(f"Depósito de {valor} realizado com sucesso na conta {conta_numero}")
            else:
                print("Conta não encontrada")
        elif op == 4:
            print("Sacar foi selecionada")
            conta_numero = input("Digite o número da conta: ")
            conta = banco.buscar_conta(conta_numero)
            if conta:
                valor = float(input("Digite o valor a ser sacado: "))
                if conta.sacar(valor):
                    print(f"Saque de {valor} realizado com sucesso na conta {conta_numero}")
                else:
                    print("Saldo insuficiente para realizar o saque")
            else:
                print("Conta não encontrada")
        elif op == 5:
            print("Ver Relatório de Transações foi selecionada")
            conta_numero = input("Digite o número da conta: ")
            conta = banco.buscar_conta(conta_numero)
            if conta:
                transacoes = conta.log_transacoes()
                if transacoes:
                    print(f"Relatório de Transações da conta {conta_numero}:")
                    for transacao in transacoes:
                        print(transacao)
                else:
                    print("Nenhuma transação encontrada para esta conta")
            else:
                print("Conta não encontrada")
        elif op == 6:
            print("Sair foi selecionada")
            break
        else:
            print("Opção inválida, por favor selecione novamente")
    print("Fim")