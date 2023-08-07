from models.acao import Acao
from utils.conexao.conexao import MyDatabase


def menu_acao():
    while True:
        print('1 - Cadastrar ação ')
        print('2 - Deletar ação ')
        print('3 - Listar ações ')
        op = input('Selecione a operação desejada: ')

        if op == '1':
            acao = Acao()
            print('Insira os dados da ação:')
            acao.set_nome(input("Insira o nome da ação:"))
            acao.set_cliente_id(input("Insira o id do cliente: "))
            salva_acao(acao)
        elif op == '2':
            acao = Acao()
            print('Insira os dados da ação que será deletada:')
            acao.set_nome(input("Insira o nome da ação:"))
            acao.set_cliente_id(input("Insira o id do cliente: "))
            deleta_acao(acao)
        elif op == '3':
            cliente_id = input("Insira o id do cliente: ")
            lista_acoes(cliente_id)
        else:
            print('Opção inválida!')

        op = input('Você deseja voltar para o menu principal? [S/N]').upper()
        if op == 'S':
            break


def salva_acao(acao):
    query = f"""INSERT INTO acao(nome , cliente_id) VALUES(%s, %s)"""

    values = (acao.get_nome(),
              acao.get_cliente_id(),
              )

    db = MyDatabase()
    try:
        db.cur.execute(query, values)
        db.conn.commit()
        db.cur.close()
    except Exception as e:
        print("Ocorreu um erro ao tentar salvar a açao: Erro recebido: ", e)
    finally:
        db.cur.close()
        db.close()


def deleta_acao(acao):
    query = f"""DELETE FROM acao WHERE nome=%s AND cliente_id=%s"""
    values = (acao.get_nome(),
              acao.get_cliente_id())

    db = MyDatabase()
    try:
        db.cur.execute(query, values)
        db.conn.commit()
        db.cur.close()
    except Exception as e:
        print("Ocorreu um erro ao tentar deletar a ação: Erro recebido: ", e)
    finally:
        db.cur.close()
        db.close()


def lista_acoes(cliente_id):
    query = "SELECT nome FROM acao WHERE cliente_id=%s"
    values = cliente_id
    db = MyDatabase()
    try:
        db.cur.execute(query, values)
        db.conn.commit()
        acoes = db.cur.fetchall()

        for acao in acoes:
            print(acao)

        db.cur.close()
        return acoes
    except Exception as e:
        print("Ocorreu um erro ao tentar listar as ações cadastradas: Erro recebido: ", e)
    finally:
        db.cur.close()
        db.close()
