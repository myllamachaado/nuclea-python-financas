from models.cliente import Cliente
from utils.cep.valida_cep import busca_cep
from utils.conexao.conexao import MyDatabase
from utils.validacoes import valida_cpf, valida_rg, valida_data_nascimento


def menu_cliente():
    while True:
        print('1 - Criar novo cliente ')
        print('2 - Editar cliente ')
        print('3 - Apagar cliente ')
        print('4 - Listar clientes ')
        op = input('Selecione a operação desejada: ')

        if op == '1':
            cliente = Cliente()
            print('Insira os dados do cliente:')
            cliente.set_nome(input('Nome: '))
            cliente.set_cpf(valida_cpf())
            cliente.set_rg(valida_rg())
            cliente.set_data_nascimento(valida_data_nascimento())
            cliente.set_cep(busca_cep(input('CEP: ')))
            cliente.set_numero_casa(input('Número da casa: '))
            print(cliente)
            salva_cliente(cliente)
        elif op == '2':
            cliente = Cliente()
            id_cliente = int(input('Insira o identificador do cliente que será alterado: '))
            print('Insira os dados atualizados do cliente:')
            cliente.set_nome(input('Nome: '))
            cliente.set_cpf(valida_cpf())
            cliente.set_rg(valida_rg())
            cliente.set_data_nascimento(valida_data_nascimento())
            cliente.set_cep(busca_cep(input('CEP: ')))
            cliente.set_numero_casa(input('Número da casa: '))
            atualiza_cliente(cliente, id_cliente)
        elif op == '3':
            id_cliente = input('Insira o id do cliente que você deseja apagar:')
            deleta_cliente(id_cliente)
        elif op == '4':
            lista_clientes()
        else:
            print('Opção inválida!')

        op = input('Você deseja voltar para o menu principal? [S/N]').upper()
        if op == 'S':
            break


def salva_cliente(cliente):
    query = f"""INSERT INTO cliente(nome , cpf, rg, data_nascimento, cep, longradouro, complemento, bairro,
                cidade, estado, numero_residencia) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    values = (cliente.get_nome(),
              cliente.get_cpf(),
              cliente.get_rg(),
              cliente.get_data_nascimento(),
              cliente.get_cep(),
              cliente.get_logradouro(),
              cliente.get_complemento(),
              cliente.get_bairro(),
              cliente.get_cidade(),
              cliente.get_estado(),
              cliente.get_numero_casa()
              )

    db = MyDatabase()
    db.cur.execute(query, values)
    db.conn.commit()
    db.cur.close()


def deleta_cliente(id_cliente):
    query = f"""DELETE FROM cliente WHERE id={id_cliente}"""
    db = MyDatabase()
    db.cur.execute(query)
    db.conn.commit()
    db.cur.close()


def atualiza_cliente(cliente, id_cliente):
    query = f"""UPDATE cliente SET nome=%s, cpf=%s, rg=%s, data_nascimento=%s, cep=%s, longradouro=%s, complemento=%s, 
                        bairro=%s, cidade=%s, estado=%s, numero_residencia=%s WHERE id=%s"""

    values = (cliente.get_nome(),
              cliente.get_cpf(),
              cliente.get_rg(),
              cliente.get_data_nascimento(),
              cliente.get_cep(),
              cliente.get_logradouro(),
              cliente.get_complemento(),
              cliente.get_bairro(),
              cliente.get_cidade(),
              cliente.get_estado(),
              cliente.get_numero_casa(),
              id_cliente
              )

    db = MyDatabase()
    db.cur.execute(query, values)
    db.conn.commit()
    db.cur.close()


def lista_clientes():
    query = "SELECT * FROM cliente"
    db = MyDatabase()
    db.cur.execute(query)
    db.conn.commit()
    clientes = db.cur.fetchall()

    for cliente in clientes:
        print(cliente)

    db.cur.close()
