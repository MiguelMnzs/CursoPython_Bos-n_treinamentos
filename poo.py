class Veiculo:
    def movimentar(self):
        print('vrummmmmmmm')

    def __init__(self, fabricante, modelo):

        # Através do ''__'' antes dos atributos eu os tornei privados, o que é chamado de encapsulamento.
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_register = None

    # metodo setter permite gravar um dado dentro do objeto
    def set_num_register(self, register):
        self.__num_register = register

    # metodo para acessar atributos privados através do getter
    def get_fab_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}')

    def get_num_register(self):
        return self.__num_register
    

    # Implementação de Heranças
class Carro(Veiculo): # Classe que vai ser herdada
    # Método __init__ será herdado.
    def movimentar(self):
        print(f'VRUMNNN VRUMNNN VRUMNNN')

class Motocicleta(Veiculo):  # Ao reutilizar um metodo estamos aplicando o conceito de polimorfismo 
    def movimentar(self):
        print('IUNNNNNNNNNNNNRNRNRNNRNNR UHNNNNN')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo) # Superclasse, a classe da qual o aviao herda.
    def get_categoria(self):
        return self.__cat
     
        
if __name__=='__main__':
    meu_veiculo = Veiculo('BMW','Perseu')
    meu_veiculo.movimentar()

    # aqui eu gravei o valor atraves do setter
    meu_veiculo.set_num_register("93838-1")
    print(f'Registro: {meu_veiculo.get_num_register()}')

    # aqui eu chamo o metodo get para exibir os atributos internos protegidos.
    meu_veiculo.get_fab_modelo() 

    # Utilizando da herança criada anteriormente
    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fab_modelo()

    seu_carro = Carro('Audi', 'A5 Sportback')
    seu_carro.movimentar()
    seu_carro.get_fab_modelo()


    moto = Motocicleta('Harley-Davidson', 'Nightster Special')
    moto.movimentar()
    moto.get_fab_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fab_modelo()
    meu_aviao.get_categoria()





