class Carro():
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.placa = None
        self.qtd_de_combustivel = 0

    
    def abastecer(self, quantidade):
        if self.qtd_de_combustivel + quantidade > 30:
            qtd_de_combustivel_anterior = self.qtd_de_combustivel
            self.qtd_de_combustivel = 30
            return qtd_de_combustivel_anterior + quantidade - 30
        else:
            self.qtd_de_combustivel += quantidade
            return 0
    
    def exibir(self):
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Placa:', self.placa)
        print('Qtd de combustível:', self.qtd_de_combustivel)


if __name__ == '__main__':
    my_car = Carro()
    my_car.marca = 'Toyota'
    my_car.modelo = 'Corolla'
    my_car.placa = 'FHA-7134'
    print('Sobrou:', my_car.abastecer(10))
    my_car.exibir()
    print('Sobrou:', my_car.abastecer(21))
    my_car.exibir()
    