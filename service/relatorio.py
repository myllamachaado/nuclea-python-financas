import yfinance as yf

from repository import acaoRepository


def obter_dados_acao():
    cliente_id = input('Insira o id do cliente: ')
    lista = list(acaoRepository.lista_acoes(cliente_id))

    if len(lista) > 0:
        nome_arquivo = "lista_ordens_cliente_id_" + cliente_id
        try:
            # Obter os dados da ação usando o Yahoo Finance (B3)
            for l in lista:
                ticker = str(l).replace("('", "").replace("',)", "")
                acao = yf.download(ticker, progress=False)

                # Exibir os dados
                with open(nome_arquivo, 'a') as arquivo:
                    arquivo.write("\n\nRelatorio da acao: " + ticker + "\n")
                    arquivo.write(str(acao.tail()))

            print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")

        except Exception as e:
            print("Erro ao obter dados da ação. Verifique o código da ação e tente novamente.")
            print(f"Detalhes do erro: {e}")
        finally:
            arquivo.close()
    else:
        print('O cliente de id=', cliente_id, ' não possui ações cadastradas. Cadastre uma ação no menu ações.')
