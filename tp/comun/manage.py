from tp.comun.classes import Cliente, Produto, Venda, itemVenda


def inclui_cliente():
    cliente = Cliente()
    nome = input("Nome: ")
    cliente.set_nome(nome)
    endereco = input("Endereco: ")
    cliente.set_endereco(endereco)
    rg = input("RG: ")
    cliente.set_rg(rg)
    nascimento = input("Nascimento: ")
    cliente.set_nascimento(nascimento)
    return cliente


def inclui_produto():
    produto = Produto()
    codigo = input("Codigo: ")
    produto.set_codigo(codigo)
    nome = input("Nome: ")
    produto.set_nome(nome)
    valor = input("Valor: ")
    produto.set_valor(valor)
    return produto


def altera_cliente(index):
    cliente = Cliente.lista[index]
    print(cliente.personal_data())
    nome = input("Nome: ")
    cliente.set_nome(nome)
    endereco = input("Endereco: ")
    cliente.set_endereco(endereco)
    rg = input("RG: ")
    cliente.set_rg(rg)
    nascimento = input("Nascimento: ")
    cliente.set_nascimento(nascimento)


def altera_produto(index):
    produto = Produto.lista[index]
    print(produto.specifications_data())
    codigo = input("Codigo: ")
    produto.set_codigo(codigo)
    nome = input("Nome: ")
    produto.set_nome(nome)
    valor = input("Valor: ")
    produto.set_valor(valor)


def vende_produto():
    venda = Venda()
    data = input("Data: ")
    venda.set_data(data)
    print("-" * 5 + " Clientes " + "-" * 20)
    for i, cliente in enumerate(Cliente.lista):
        nome = cliente.personal_data()[0]
        print(f"{i:02d}: {nome}")
    print("-" * 35)
    try:
        index = int(input("Cliente: "))
        cliente = Cliente.lista[index]
        venda.set_cliente(cliente)
    except:
        print("Opcao# invalida.")
        return
    print("-" * 5 + " Produtos " + "-" * 20)
    for i, produto in enumerate(Produto.lista):
        nome  = produto.specifications_data()[1]
        valor = produto.specifications_data()[2]
        print(f"{i:02d}: {nome}\t{valor}")
    print("-" * 35)
    print("digite # enter, f para sair")
    produtos_loop = True
    while produtos_loop:
        index = input()
        if index == "f":
            produtos_loop = False
        else:
            try:
                index = int(index)
                produto = Produto.lista[index]
                venda.set_item(produto)
                venda.total(produto.specifications_data()[2])
                item = itemVenda()
                item.set_produto(produto)
            except:
                print("Opcao# invalida.")

    return venda
