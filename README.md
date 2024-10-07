# Sistema Bancário

Este é um exemplo de aplicação de sistema bancário desenvolvido em Python. A aplicação permite a criação de clientes e contas, além de realizar operações bancárias como depósitos, saques, transferências e consultas de saldo.

## Estrutura do Projeto

- `main.py`: Arquivo principal que inicializa o sistema e exibe o menu principal.
- `menu.py`: Classe responsável por exibir o menu e capturar a opção selecionada pelo usuário.
- `banco.py`: Classe que representa o banco e gerencia clientes e contas.
- `cliente.py`: Classe que representa um cliente do banco.
- `conta.py`: Classe que representa uma conta bancária.
- `operacoes.py`: Funções que realizam as operações bancárias.

## Funcionalidades

1. **Criar Cliente**: Permite a criação de um novo cliente.
2. **Criar Conta**: Permite a criação de uma nova conta para um cliente existente.
3. **Depósito**: Realiza um depósito em uma conta existente.
4. **Saque**: Realiza um saque de uma conta existente.
5. **Transferência**: Realiza uma transferência entre duas contas.
6. **Consultar Saldo**: Consulta o saldo de uma conta.
7. **Listar Clientes**: Lista todos os clientes cadastrados.
8. **Listar Contas de um Cliente**: Lista todas as contas de um cliente específico.
9. **Sair**: Encerra o programa.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o arquivo `main.py`:
   ```sh
   python main.py