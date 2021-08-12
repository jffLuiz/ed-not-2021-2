#algoritmo de busca binaria
#dada uma lista, que deve ser previamente ordenada, e um valor de busca, divide a lista em duas metades e procura pelo valor de busca apenas na metade onde o valor poderia estar. Novas subdivisoes são feitas até que se encontre o valor de busca ou que reste apenas uma sublista vazia, quando se conclui que o valor de busca não existe na lista

from time import time 
from data.lista_nomes import nomes

comps=0

def busca_binaria(lista, valor_busca):
    '''
        funcão que implementa o algoritmo de busca binaria
        retorna a posição onde valor_busca foi encontrado ou o valor convencional -1 se o valor_busca não existir na lista
    '''
    ini = 0 #primeira posição
    fim = len(lista)-1 #ultima posição

    while ini <= fim:
        meio=(ini+fim)//2 # // : volta somente o valor inteiro da divisão 

        #1º caso: lista[meio] é iqual a valor_dusca
        if lista[meio] == valor_busca: #encontrou
            return meio #meio é a posição onde valor_busca está na lista
        #2ºcasi: valor_busca é menor que lista[meio]
        elif valor_busca < lista[meio]:
            fim=meio-1 #descartando a segunda metade da lista
        #3ºcaso: valor_busca é maior que lista[meio]
        else: 
            ini=meio+1 #descarta a 1º metade da lista
    
    #4º caso: valor_busca não encontrado na lista
    return -1


hora_ini = time()
print(f"posição de fausto: {busca_binaria(nomes, 'FAUSTO')}")
hora_fim = time()
print(f"tempo gasto procurando fausto: {(hora_fim - hora_ini)*1000}ms")

hora_ini = time()
print(f"posição de zuleica: {busca_binaria(nomes, 'ZULEICA')}")
hora_fim = time()
print(f"tempo gasto procurando zuleica: {(hora_fim - hora_ini)*1000}ms")

hora_ini = time()
print(f"posição de orkutilson: {busca_binaria(nomes, 'ORKUTILSON')}")
hora_fim = time()
print(f"tempo gasto procurando orkutilson: {(hora_fim - hora_ini)*1000}ms")

hora_ini = time()
print(f"posição de Belerina: {busca_binaria(nomes, 'BELERINA')}")
hora_fim = time()
print(f"tempo gasto procurando belerina: {(hora_fim - hora_ini)*1000}ms")

hora_ini = time()
print(f"posição de Jefferson: {busca_binaria(nomes, 'JEFFERSON')}")
hora_fim = time()
print(f"tempo gasto procurando Jefferson: {(hora_fim - hora_ini)*1000}ms")
