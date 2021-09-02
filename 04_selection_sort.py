#Algoritmo de ordenação selection sort

#isola (seleciona) o primeiro elemento da lista e, em seguida, encontra o menor valor no restante da lista. Se o valor encontrado for menor que o valor selecionado, efetua a troca. Em seguida, isola o segundo numero da lista, buscando pelo menor valor das posições subsequentes. Faz a troca entre os dois valores, se necessário. Continua o processo, até isolar o penultimo elemento da lista.

comps=0 #numero de comparações
passadas=0 #numero de passadas
trocas=0 #numero de trocas

def selection_sort(lista):
    '''função que implementa o algoritmo de ordenação selection sort'''
    global comps, passadas, trocas 
    comps=0 
    passadas=0 
    trocas=0 
    #seleciona(isola) o elemento que será comparado
    for pos_sel in range(len(lista)-1):
        passadas+=1

        pos_menor=pos_sel+1
        #rotina para encontar o menor numero no resto da lista
        #percurso da lista da posição i+2 até o fim
        for j in range(pos_sel+2, len(lista)):
            comps+=1
            #se o elemento da posição atual [j] for menor que o elemento na posição do menor (pos_menor), atualizamos pos_menor
            if lista[j] < lista[pos_menor]:
                pos_menor=j
        #comparamos lista[sel] com lista[pos_menor] e se segundo for menor que o primeiro, efetuamos a troca entre eles

        comps+=1
        if lista[pos_menor] < lista [pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas+=1
####################################################

#valores das variaveis no inicio do selection sort: 
#pos_sel: 0 (onde esta o 88)
#pos_menor: 1 (onde esta o 44)
#j: 2 (onde esta o 33)
nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]
selection_sort(nums)
print(nums)
print(f"Embaralhado = Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

#não é o pior caso
nums = [99,88,77,66,55,44,33,22,11,0]
selection_sort(nums)
print(f"Não é o Pior caso = Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

#melhor caso
nums = [0,11,22,33,44,55,66,77,88,99]
selection_sort(nums)
print(f"Melhor caso = Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

nums=[99,0,11,22,33,44,55,66,77,88]
#não é o pior caso
nums=[99,0,11,22,33,44,55,66,77,88]
selection_sort(nums)
print(f"Pior caso = Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

##################################################

from data.nomes_desord import nomes
from time import time
import tracemalloc

#nomes_parcial = nomes[:3000] #usa apenas os primeiros 20mil nomes -1

ini=time()
tracemalloc.start()

# selection_sort(nomes_parcial)
selection_sort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim=time()

#print(nomes_parcial)
print(nomes)
print(f"Tempo: {fim-ini}")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

tracemalloc.stop()