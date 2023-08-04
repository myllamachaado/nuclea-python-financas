from repository.ClienteRepository import menu_cliente


def cadastro_acao():
    pass


def analisar_carteira():
    pass


def imprimir_relatorio():
    pass


if __name__ == '__main__':

    while True:
        print('Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. '
              'Selecione uma das opções abaixo:')
        print('1 - Cliente')
        print('2 - Cadastra Ação')
        print('3 - Realizar Análise da Carteira')
        print('4 - Imprimir Relatório da Carteira')
        print('5 - Sair')
        r = int(input('Selecione uma opção: '))

        if r == 5:
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            break

        elif r == 1:
            menu_cliente()

        elif r == 2:
            cadastro_acao()

        elif r == 3:
            analisar_carteira()

        elif r == 4:
            imprimir_relatorio()

        else:
            print('Opção inválida, selecione outra opção!')
