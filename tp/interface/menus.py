import os
from tp.comun.manage import *

try:
    from simple_term_menu import TerminalMenu
except ImportError as impErr:
    print(f"[Error]: Failed to import --> {impErr.args[0]}.")
    print("Use: pip install simple_term_menu")
    exit(1)


def cls():
    os.system("cls" if os.name=="nt" else "clear")


def menu_back():
    input("Presione Enter para continuar...")
    cls()


def client_lista():
    for i, cliente in enumerate(Cliente.lista):
        nome = cliente.personal_data()[0]
        print(f"{i:02d}: {nome}")


def product_lista():
    for i, produto in enumerate(Produto.lista):
        nome = produto.specifications_data()[1]
        print(f"{i:02d}: {nome}")


def show_clients():
    for i, cliente in enumerate(Cliente.lista):
        nome  = cliente.personal_data()[0]
        local = cliente.personal_data()[1]
        rg    = cliente.documents_data()[0]
        birth = cliente.documents_data()[1]
        print(f"{i:02d}: {nome}\t{rg}\t{birth}\n    {local}")
    menu_back()


def show_vendas():
    for i, venda in enumerate(Venda.lista):
        numero  = venda.sell_data()[0]
        data    = venda.sell_data()[1]
        cliente = venda.sell_data()[2].personal_data()[0]
        total   = venda.sell_data()[3]
        print(f"{numero:02d}: [{data}] {cliente}\t{total}")
    menu_back()


def show_products():
    for i, produto in enumerate(Produto.lista):
        codigo = produto.specifications_data()[0]
        nome   = produto.specifications_data()[1]
        valor  = produto.specifications_data()[2]
        print(f"{i:02d}: [{codigo}] {nome}\t{valor}")
    menu_back()


def validate(manage):
    try:
        index = int(input("Opcao#: "))
        manage(index)
    except:
        print("Opcao# invalida.")
    menu_back()


def remove_object(Class):
    try:
        index = int(input("Opcao#: "))
        Class.lista[index].remove()
    except:
        print("Opcao# invalida.")
    menu_back()


def menus():
    cls()
    opt_inicial = ["[c] clientes", "[p] produtos", "[v] vendas","[q] sair"]
    opt_submenu = ["[i] incluir", "[a] alterar", "[l] listar", "[e] excluir", "[b] voltar"]
    opt_vendas  = ["[v] vender", "[l] listar vendas", "[b] voltar"]
    title = "UFSJ/CLP 2022/1 : TP1"
    loop = True
    while loop:
        subtitle = "\nMenu Principal"
        menu_main = TerminalMenu(opt_inicial, title=title + subtitle)
        option = menu_main.show()
        if option == 0:
            subtitle = "\nClientes"
            sub_loop = True
            while sub_loop:
                submenu = TerminalMenu(opt_submenu, title=title + subtitle)
                option = submenu.show()

                if option == 0:
                    print(title + subtitle)
                    inclui_cliente()
                    cls()
                elif option == 1:
                    print(title + subtitle)
                    client_lista()
                    validate(altera_cliente)
                elif option == 2:
                    print(title + subtitle)
                    show_clients()
                elif option == 3:
                    print(title + subtitle)
                    client_lista()
                    remove_object(Cliente)
                elif option == 4:
                    sub_loop = False

        elif option == 1:
            subtitle = "\nProdutos"
            sub_loop = True
            while sub_loop:
                submenu = TerminalMenu(opt_submenu, title=title + subtitle)
                option = submenu.show()

                if option == 0:
                    print(title + subtitle)
                    inclui_produto()
                    cls()
                elif option == 1:
                    print(title + subtitle)
                    product_lista()
                    validate(altera_produto)
                elif option == 2:
                    print(title + subtitle)
                    show_products()
                elif option == 3:
                    print(title + subtitle)
                    product_lista()
                    remove_object(Produto)
                elif option == 4:
                    sub_loop = False

        elif option == 2:
            subtitle = "\nVendas"
            sub_loop = True
            while sub_loop:
                submenu = TerminalMenu(opt_vendas, title=title + subtitle)
                option = submenu.show()
                if option == 0:
                    print(title + subtitle)
                    vende_produto()
                    cls()
                if option == 1:
                    print(title + subtitle)
                    show_vendas()
                if option == 2:
                    sub_loop = False

        elif option == 3:
            loop = False
