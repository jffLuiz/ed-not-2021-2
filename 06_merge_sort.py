#   ALGORITMO DE ORDENAÇÃO MERGE SORT
#
#   No processo de ordenação, esse algoritmo "desmonta" o vetor original
#   contendo N elementos até obter N vetores de apenas um elemento cada um.
#   Em seguida, usando a técnica de mesclagem (merge), "remonta" o vetor,
#   dessa vez com os elementos já em ordem.

comps = 0
divisoes = 0 
juncoes = 0

def merge_sort(lista):
    ''' função que complementa o algorimo merge sorte usando o metodo recursivo'''

    # não podemos zerar as variaveis globais de estatistica dentro da função , pq ela é recursiva, e resetaria a contagem a cada chamada
    global comps, divisoes, juncoes
    

    #print(f'lista recebida: {lista}')

    #só continua se a lista tiver mais de um elemento
    if len(lista)<=1:
        return lista
    
    meio = len(lista)//2 #calcular o meio calculando apenas a divisão inteira

    #gerar cópia da primeira metade da lista
    lista_esq = lista[:meio] #do inicio ao meio -1

    #gerar cópia da segunda metade da lista
    lista_dir = lista[meio:] #do meio ao fim

    divisoes += 1

    #chamamos recursivamente a função para continuar
    #repartindo a lista em metades
    lista_esq = merge_sort(lista_esq)
    lista_dir = merge_sort(lista_dir)

    # print(f'>>> lista_esq: {lista_esq}')
    # print(f'>>> lista_dir: {lista_dir}')

    #junta as duas metades em uma unica lista, ordenada
    pos_esq = 0
    pos_dir = 0
    ordenada = [] #lista vazia

    #compara os elementos de cada lista entre si e insere na lista ordenada o que for menor
    while pos_esq < len(lista_esq) and pos_dir < len(lista_dir):
        #o elemento que se enconta na lista da esquerda é menor que o que se encontra na lista da direita
        if lista_esq[pos_esq] < lista_dir[pos_dir]:
            ordenada.append(lista_esq[pos_esq])
            pos_esq += 1
        else:
            ordenada.append(lista_dir[pos_dir])
            pos_dir += 1

        comps +=1 
    
    sobra = None # a sobra da lista que ficou para trás

    if (pos_esq < pos_dir): #house sobra a esquerda
        sobra = lista_esq[pos_esq:] #sobra da pos_esq até o final
    else: #houve sobra a direita
        sobra = lista_dir[pos_dir:] #sobra da pos_dir até o final 

    # print(f'>>> final ordenada: {ordenada+sobra}')

    juncoes += 1 
    
    return ordenada + sobra # "soma" de duas listas

########################################################
comps = 0
divisoes = 0 
juncoes = 0

nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

nums_ord = merge_sort(nums)

print(nums_ord)

##############################################
from data.nomes_desord import nomes
from time import time
import tracemalloc
import psutil

comps = 0
divisoes = 0 
juncoes = 0

ini=time()
tracemalloc.start() #inicia a medição de consumo de memória

nomes_ord = merge_sort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim=time()

#print(nomes_parcial)
print(nomes_ord)
print(f"Tempo: {fim-ini}")
print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')
print(f"comparações: {comps} ; divisoes: {divisoes} ; junçoes: {juncoes}")



tracemalloc.stop() #finaliza a medição de consumo de memória

print('The CPU usage is: ', psutil.cpu_percent(4))