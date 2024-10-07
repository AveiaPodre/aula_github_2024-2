from menu import Menu
from banco import Banco
import operacoes

if __name__ == "__main__":
    banco = Banco()
    main_menu = Menu(["Criar Cliente", "Criar Conta", "Depósito", "Saque", "Transferência", "Consultar Saldo", "Listar Clientes", "Listar Contas de um Cliente", "Sair"], "Menu Principal")

    while True:
        opcao = main_menu.get_selection()
        if opcao == 1:
            operacoes.criar_cliente(banco)
        elif opcao == 2:
            operacoes.criar_conta(banco)
        elif opcao == 3:
            operacoes.realizar_deposito(banco)
        elif opcao == 4:
            operacoes.realizar_saque(banco)
        elif opcao == 5:
            operacoes.realizar_transferencia(banco)
        elif opcao == 6:
            operacoes.consultar_saldo(banco)
        elif opcao == 7:
            operacoes.listar_clientes(banco)
        elif opcao == 8:
            operacoes.listar_contas_cliente(banco)
        elif opcao == 9:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")