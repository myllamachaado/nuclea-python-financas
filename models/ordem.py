class Ordem:

    def __init__(self):
        self.id = ""
        self.cliente_id = ""
        self.nome = ""
        self.ticket = ""
        self.valor_compra = ""
        self.quantidade_compra = ""
        self.data_compra = ""

    def get_id(self):
        return self.id

    def set_id(self, x):
        self.id = x

    def get_nome(self):
        return self.nome

    def set_nome(self, x):
        self.nome = x

    def get_ticket(self):
        return self.ticket

    def set_ticket(self, x):
        self.ticket = x

    def get_valor_compra(self):
        return self.valor_compra

    def set_valor_compra(self, x):
        self.valor_compra = x

    def get_quantidade_compra(self):
        return self.quantidade_compra

    def set_quantidade_compra(self, x):
        self.quantidade_compra = x

    def get_data_compra(self):
        return self.data_compra

    def set_data_compra(self, x):
        self.data_compra = x

    def get_cliente_id(self):
        return self.cliente_id

    def set_cliente_id(self, x):
        self.cliente_id = x
