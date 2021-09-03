# ALGORITMO DE ORDENAÇÃO QUICK SORT

# Escolhe um dos elementos do vetor para ser o pivô (na nossa implementação,
# o último elemento) e, na primeira passada, divide o vetor, a partir da posição
# final do vetor, em um subvetor à esquerda contendo apenas valores menores que
# o pivô e outro subvetor à direita, que contém apenas valores maiores que o pivô.# 
# Em seguida, recursivamente, repete o processo em cada um dos subvetores até que
# todo o vetor esteja ordenado.

passadas=0
comps=0
trocas=0

def quick_sort(lista, ini=0, fim=None):
    '''
        funcao que complementa o algoritmo de ordenação quick sort de forma recursiva
    ''' 

    #se fim for None, então consideramos ultima posição da lista
    if fim is None:
        fim = len(lista)-1
    # para continuarmos, precisamos que a lista tenha pelo menos dois ementos para ordenar
    if fim <= ini:
        return  #sai da função sem fazer nada


    global passadas, comps, trocas

    passadas+=1

    pivot = fim #o pivo é o ultimo elemento
    div = ini -1   # o divisor inicia antes do primeiro elemento

    # percorre a lista da posição ini até a posição fim -1
    for i in range(ini, fim):
        comps+=1
        if lista[i] < lista[pivot]:
            div+=1 #incrementa o divisor
            if div != i: #caso nao sejam o mesmo elemento
                lista[div], lista[i] = lista[i], lista[div] #lista[div] e lista[i] trocam de lugar entre si
                trocas+=1
    
    #depois que o percurso de i acaba, div ainda é incrementado mais uma vez
    div += 1

    #colocamos o pivo em seu lugar definitivo, a troca acontece se o valor do pivo for menor que o valor da posição div
    comps+=1
    if lista[pivot] < lista[div] and pivot != div:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas+=1

    #chamamos recursivamente a funcao para a sublista a esquerda da posição div
    quick_sort(lista, ini, div-1)

    # chamamos recursivamente a função para a sublista a direita da posição div
    quick_sort(lista, div + 1, fim)

####################################

nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

quick_sort(nums)

print(nums)

print(f"passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

###########################

from data.nomes_desord import nomes
from time import time
import tracemalloc
import psutil

passadas=0
comps=0
trocas=0

#nomes_parcial = nomes[:3000] #usa apenas os primeiros 20mil nomes -1

ini=time()
tracemalloc.start()

# selection_sort(nomes_parcial)
quick_sort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim=time()

#print(nomes_parcial)
print(nomes)
print(f"Tempo: {fim-ini}")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

tracemalloc.stop()

print('The CPU usage is: ', psutil.cpu_percent(4))

