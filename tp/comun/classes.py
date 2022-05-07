from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def set_nome(self):
        ...

    @abstractmethod
    def set_endereco(self):
        ...

    def personal_data(self):
        return (self.nome, self.endereco)


class Totalizavel(ABC):
    @abstractmethod
    def total(self):
        ...


class Cliente(Pessoa):
    lista = []

    def __init__(self):
        Cliente.lista.append(self)

    def set_nome(self, nome):
        self.nome = nome

    def set_endereco(self, endereco):
        self.endereco = endereco

    def set_rg(self, rg):
        self.rg = rg

    def set_nascimento(self, nascimento):
        self.nascimento = nascimento

    def documents_data(self):
        return (self.rg, self.nascimento)

    def remove(self):
        Cliente.lista.remove(self)


class Produto:
    lista = []

    def __init__(self):
        Produto.lista.append(self)

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nome(self, nome):
        self.nome = nome

    def set_valor(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

    def specifications_data(self):
        return [self.codigo, self.nome, self.valor]

    def remove(self):
        Produto.lista.remove(self)


class Venda(Totalizavel):
    lista = []
    numero = 0

    def __init__(self):
        self.itens = []
        self.totaldavenda = 0
        Venda.lista.append(self)

    def set_data(self, data):
        self.data = data
        self.numero = Venda.numero
        Venda.numero += 1

    def set_cliente(self, Client):
        self.client = Client

    def set_item(self, Produto):
        self.itens.append(Produto)

    def sell_data(self):
        return [self.numero, self.data,
            self.client, self.totaldavenda]

    def total(self, valor):
        self.totaldavenda += int(valor)


class itemVenda(Totalizavel):

    def __init__(self):
        self.totaldavenda = 0

    def set_produto(self, Produto):
        self.produto = Produto
        self.valor = Produto.get_valor()
        self.total(self.valor)

    def total(self, valor):
        self.totaldavenda += int(valor)