from repository.acaoRepository import menu_acao
from repository.clienteRepository import menu_cliente
from service.analiseCarteira import analisa_carteira
from service.relatorio import obter_dados_acao


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
            menu_acao()

        elif r == 3:
            analisa_carteira()

        elif r == 4:
            obter_dados_acao()

        else:
            print('Opção inválida, selecione outra opção!')
