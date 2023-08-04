from validate_docbr import CPF
from datetime import datetime
import re


def valida_cpf():
    cpf_validador = CPF()

    while True:
        cpf = input("CPF: ")
        resultado_validacao = cpf_validador.validate(cpf)
        if resultado_validacao:
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            return cpf_formatado
        else:
            print("CPF inválido, digite novamente: ")


def valida_rg():
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

    while True:
        rg = input("RG: ")
        if re.match(padrao_rg, rg):
            return rg
        else:
            print("RG inválido. Tente novamente:")


def valida_data_nascimento():
    while True:
        data_nascimento = input("Data Nascimento: ")
        try:
            data_convertida = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            data_atual = datetime.now().date()

            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")
            else:
                print("A data de nascimento não pode ser maior que a data atual.")
        except ValueError as e:
            print("Recebei um erro: ", e, ". Digite novamente a data de nascimento.")

