#classe é uma estrutura que representa conjuntamente dados e algoritmos. A classe é como uma "forma de bolo", com a qual podemos criar diferentes "bolos" (objetos). Cada "bolo" (objeto) pode ser feito com seus proprios ingredientes (dados) e modos de fazer (algoritmos), mas terão sempre o formato determinado pela forma (classe)
from math import pi

class FormaGeometrica():
    #dados
    #quando pertencem a uma classe, ganham o nome de Atributos
    #base = 0
    #altura = 0
    #tipo = "R" #retangulo

    #algoritmos
    #são representados por funções que, quando se encontram dentro de uma classe, ganham o nome de Métodos

    #este metodo é executado quando um objeto é criado a partir de uma classe (construtor)
    def __init__(self, base, altura, tipo = "R"):
        #recebe os valores passados ao construtor e os armazena dentro dos atributos
        #print(f"base: {base} ({type(base)}), altura: {base} ({type(altura)}),")

        # if type(base) not in [int,float] or base<=0:
        #     raise Exception("a base deve ser maior que zero")
        # elif type(altura) not in [int,float] or altura<=0:
        #     raise Exception("a altura deve ser maior que zero")
        # elif tipo not in ["R","T","E"]:
        #     raise Exception("o tipo deve ser R, T ou E")

        #ajustando o valor dos atributos para privado ( adicionar __ no inicio do nome)
        # self.__base = base
        # self.__altura = altura
        # self.__tipo = tipo

        #ajustando o valor inicial via setters das propriedades
        self.base = base
        self.altura = altura
        self.tipo = tipo
    
    #Getter é um método que possibilita saber o valor de um atributo privado do lado de fora da classe

    def __get_base(self):
        return self.__base
    
    #setter é um metodo que possibilita alterar o valor de um atributo privado inclusive do lado de fora da classe

    def __set_base(self, valor):

        if type(valor) not in [int,float] or valor<=0:
            raise Exception(" * a base deve ser maior que zero")

        self.__base = valor

    #property "esconde" as funções getter e setter dentro do nome de um atributo, tornando mais simples a manipulação
    base = property(__get_base, __set_base)

    #essas linha começadas com @ são chamadas de "decorators"
    #os decorators instruem o python a criar uma property com um getter e um setter na hora da execução
    @property
    def altura(self):   #getter para a propriedade chamada "altura"
        return self.__altura
    
    @altura.setter
    def altura(self, valor): #setter para a propriedade chamada "altura"
        if type(valor) not in [int, float] or valor <=0 :
            raise Exception(" ** a base deve ser maior que zero")   
        
        self.__altura = valor  


    @property 
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        if valor not in ["R","T","E"]:
            raise Exception(" ** o tipo deve ser R, T ou E")
        self.__tipo = valor

    #um método é uma função que, inserida dentro de uma classe, pode acessar seus dados (atributos) e manula-los
    def calc_area(self):
        if self.tipo == "R": #retangulo
            return self.base * self.altura
        elif self.tipo == "T": #triangulo
            return self.base * self.altura / 2
        else: #elipse, tipo E
            return (self.base/2) * (self.altura/2) * pi


##########################################

#criando objetos (instanciar) a partir da classe

retangulo1 = FormaGeometrica(15,10, "R") #chama o __init__
triangulo1 = FormaGeometrica(6.4, 9, "T")

print(f"area de uma forma {retangulo1.tipo} de {retangulo1.base}x{retangulo1.altura} = {retangulo1.calc_area()}")
print(f"area de uma forma {triangulo1.tipo} de {triangulo1.base}x{triangulo1.altura} = {triangulo1.calc_area()}")

#print(f"[retangulo1] base: {retangulo1.get_base()}")

#retangulo1.__base = 5 #nao funciona
#retangulo1.set_base(9.2)
#retangulo1.base = 9  #vai executar o set_base da classe
#print(f"[retangulo1] base: {retangulo1.get_base()}")
#retangulo1.set_base(12.5)

#retangulo1.__base = 0
#triangulo1.__tipo = "yadayada"

#problematico = FormaGeometrica(7.2, 5, "Q")

#print(f"[retangulo1] base: {retangulo1.base}")

#print(f"[retangulo1] base: {retangulo1.__base}, altura: {retangulo1.__altura}, tipo: {retangulo1.__tipo}")

#print(f"[triangulo1] base: {triangulo1.__base}, altura: {triangulo1.__altura}, tipo: {triangulo1.__tipo}")

#print(f"[problematico] base: {problematico.base}, altura: {problematico.altura}, tipo: {problematico.tipo}")

#print(f"[retangulo1] base: {retangulo1.get_base()}")

