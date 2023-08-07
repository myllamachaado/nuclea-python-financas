class Acao:

    def __init__(self):
        self.id = ""
        self.nome = ""
        self.cliente_id = ""

    def get_id(self):
        return self.id

    def set_id(self, x):
        self.id = x

    def get_nome(self):
        return self.nome

    def set_nome(self, x):
        self.nome = x

    def get_cliente_id(self):
        return self.cliente_id

    def set_cliente_id(self, x):
        self.cliente_id = x