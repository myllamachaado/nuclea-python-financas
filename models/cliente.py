class Cliente:

    def __init__(self):
        self.nome = ""
        self.cpf = ""
        self.rg = ""
        self.data_nascimento = ""
        self.cep = ""
        self.logradouro = ""
        self.complemento = ""
        self.bairro = ""
        self.cidade = ""
        self.estado = ""
        self.numero_casa = ""

    def get_nome(self):
        return self.nome

    def set_nome(self, x):
        self.nome = x

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, x):
        self.cpf = x

    def get_rg(self):
        return self.rg

    def set_rg(self, x):
        self.rg = x

    def get_data_nascimento(self):
        return self.data_nascimento

    def set_data_nascimento(self, x):
        self.data_nascimento = x

    def get_cep(self):
        return self.cep

    def set_cep(self, x):
        self.cep = x['CEP']
        self.logradouro = x['Logradouro']
        self.complemento = x['Complemento']
        self.bairro = x['Bairro']
        self.cidade = x['Cidade']
        self.estado = x['Estado']

    def get_numero_casa(self):
        return self.numero_casa

    def set_numero_casa(self, x):
        self.numero_casa = x

    def get_logradouro(self):
        return self.logradouro

    def get_complemento(self):
        return self.complemento

    def get_bairro(self):
        return self.bairro

    def get_cidade(self):
        return self.cidade

    def get_estado(self):
        return self.estado