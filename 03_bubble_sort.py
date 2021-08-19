# algoritmo de ordenação bubble sort
#percorre a lista a ser ordenada em sucessivas passadas, trocando elemento adjacentes entre si quando o segundo for menor que o primeiro. efetua tantas passadas quanto necessarias, até que, na ultima passada, nenhuma troca seja efetuada.

#variaveis globais
comps=0 #numero de comparações
passadas=0 #numero de passadas
trocas=0 #numero de trocas

def bubble_sort(lista):
    '''função que implementa o algoritmo de ordenação bubble sort '''

    global comps, passadas, trocas
    comps=0 
    passadas=0 
    trocas=0

    while True: #loop eterno
        passadas+=1
        trocou = False
        #loop na lista até o penultimo elemento: len(lista) - 2
        #ex: em uma lista de 10 elementos, len(lista) == 10 ... a ultima posição estará em len(lista) -1, ou seja 9 -> range(len(lsita)) ... a penuntima posição estará em len(lista) - 2, ou seja, 8 -> range(len(lista)-1)
        for i in range(len(lista)-1): #inicia nova passada
            comps+=1
            if lista[i+1] < lista[i]: #é necessario trocar
                lista[i+1], lista[i] = lista[i], lista[i+1] #faz a troca
                trocas+=1
                trocou=True
        #se não houve troca, a lista esta ordenada e podemos interromper o loop while
        if not trocou: #trocou == false
            break # interrompe o while

# nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

#pior caso
# nums = [99,88,77,66,55,44,33,22,11,0]

#melhor caso
nums = [0,11,22,33,44,55,66,77,88,99]

bubble_sort(nums)

print(nums)

print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

#####################################################################

from data.nomes_desord import nomes
from time import time

nomes_parcial = nomes[:30000] #usa apenas os primeiros 20mil nomes -1

ini=time()
bubble_sort(nomes_parcial)
fim=time()

print(nomes_parcial)
print(f"Tempo: {fim-ini}")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")


