import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

from repository import acaoRepository


def analisa_carteira():
    # Definir o período de data desejado

    start_date = input('Insira a data inicial da busca (yyyy-mm-dd): ')
    end_date = input('Insira a data final da busca (yyyy-mm-dd): ')
    cliente_id = input('Insira o id do cliente: ')

    lista = list(acaoRepository.lista_acoes(cliente_id))

    if len(lista) > 0:
        # Criar um DataFrame vazio
        df = pd.DataFrame()
        # Baixar os dados para cada ação e adicionar ao DataFrame
        for i in lista:
            cotacao = yf.download(i, start=start_date, end=end_date)
            df[i] = cotacao['Adj Close']
        # Plotar as séries de preços do DataFrame
        df.plot(figsize=(15, 10))
        plt.xlabel('Anos')
        plt.ylabel('Valor Ticket')
        plt.title('Variação de valor das ações')
        plt.legend()
        plt.show()
    else:
        print('O cliente de id=', cliente_id, ' não possui ações cadastradas em seu nome. '
                                              'Cadastre uma ação para ter acesso ao gráfico!')
