# dicionario é uma estrutura da linguagem python capaz de armazenar multiplos valores em uma unica variavel, por meio de pares de chave-valor

pessoa = {
    #"nome" é a chave
    #"fula de tal" é o valor
    "nome": "fulano de tal",
    "sexo": "M",
    "idade": 39,
    "peso": 76,
    "altura": 1.82
}

# calcular IMC
imc = pessoa["peso"] / (pessoa["altura"]**2)

print(f"o imc da {pessoa['nome']} é {imc}.")

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R" #retangulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T" #triangulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E" #elipse
}

forma4 = {
    "base": 10,
    "altura": 10,
    "tipo": "W" #tipo nao reconhecido
}

forma5 = {
    "legume": "batata",
    "fruta": "abacate",
    "tipo": "T" 
}

from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R": #retangulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T": #triangulo
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E": #elipse
        return forma["base"] / 2 * forma["altura"] / 2 * pi
    else:
        #gera um erro
        raise Exception("tipo de forma não reconhecida.")

print(f"area de um retangul de 7.5x12: {calcular_area(forma1)}")

print(f"area de um triangulo de 6x2.5: {calcular_area(forma2)}")

print(f"area de uma elipse de 5x3: {calcular_area(forma3)}")

#print(f"area de uma forma desconhecida de 10x10: {calcular_area(forma4)}")

print(f"area de uma forma desconhecida de ?x?: {calcular_area(forma5)}")