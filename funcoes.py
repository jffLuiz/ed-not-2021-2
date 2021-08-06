#importar o valor da constante pi
#math é o nome da biblioteca onde pi se encontra 
from math import pi

#funcao  é um trecho de código que tem um nome e pode receber informações externas para fazer seu trabalho. opcionalmente uma funcao pode tbm produzir um valor de resultado. Uma funcao é definida apenas uma vez e pode ser utilizada (chamada) varias vezes, evitando repetições no código.
#existem funcoes ja providas pela linguagem (funcoes internas), como por exemplo len(), range() e sort(), e podemos definir tbm nossas proprias funcoes.

#os termos que aparecem entre parenteses são chamados de parametros ou argumentos
def imc(peso, altura): #definiçaõ (ou declaração) da funcao
    """
        funcao que calcula o indice de massa corporal (imc)
    """
    #trechos entre aspas tripas são um tipo especial de comentario chamado docstring, e servem para documentar o propósito de uma funcao ou classe
    return peso/(altura**2)

# float(): converte o valor informado em um numero com casas decimais (floating point)
p = float(input('informe o peso da pessoa: '))
a = float(input('informe a altura da pessoa: '))

#fazendo uma chama a funcao imc()
resultado = imc(p,a)
print(f'o imc é de {resultado}')


def area_forma(base, altura, forma):
    """
        função que calcula a area de uma das seguintes formas geometricas: retangulo, triangulo ou elipse
        parametro forma:
        "R" == retangulo (parametro opcional com valor padrão)
        "T" == triangulo
        "E" == elipse
    """
    area=0
    if forma == 'R': #retangulo
        area=base*altura
    elif forma == 'T': #triangulo
        area=base*altura/2
    elif forma == 'E': #elipse
        area=(base/2)*(altura/2)*pi
    return area

print("----------")
print(f"retangulo 7.5x11: {area_forma(7.5,11,'R')}")

print("----------")
print(f"triangulo 8x12: {area_forma(8,12,'T')}")

print("----------")
print(f"circulo 15x15: {area_forma(15,15,'E')}")

print("----------")
print(f"quadrado 9.5x9.5: {area_forma(9.5,9.5, 'R')}")