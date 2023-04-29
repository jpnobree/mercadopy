from utils.helper import formata_float_str_moeda

class Product:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Product.contador
        self.__name = str = nome
        self.__preco = float = preco
        Product.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo


    @property
    def nome(self: object) -> str:
        return self.__name


    @property
    def preco(self: object) -> float:
        return self.__preco


    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nPreço: {formata_float_str_moeda(self.__preco)}'

