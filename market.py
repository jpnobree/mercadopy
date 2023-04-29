from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import formata_float_str_moeda


products: List[Product] = []
carrinho: List[Dict[Product, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('===============================')
    print('========= Bem vindo(a) ========')
    print('=======  Nobre Shop  ==========')
    print('===============================')

    print('Selecione uma opção abaixo:')
    print('1 - Cadastrar o produto')
    print('2 - Listar o produto')
    print('3 - Comprar o produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de produto')
    print('===================')
    
    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    product: Product = product(nome, preco)

    products.append(product)

    print(f'O produto {product.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu(2)


def listar_produto() -> None:
    if len(products) > 0:
        print('Listagem de produtos')
        print('--------------------')
        for product in products:
            print(product)
            print('----------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()



def comprar_produto() -> None:
    pass

def visualizar_carrinho() -> None:
    pass

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('--------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()

def pega_produto_por_codigo(codigo: int) -> None:
    p: Product = None


    for product in products:
        if product.codigo == codigo:
            p = product
    return p

if __name__ == '__main__':
    main()

