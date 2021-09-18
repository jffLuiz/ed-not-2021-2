
def merge_sort(lista):
    ''' função que complementa o algorimo merge sorte usando o metodo recursivo'''
   
    if len(lista)<=1:
        return lista
    
    meio = len(lista)//2 
    lista_esq = lista[:meio]
    lista_dir = lista[meio:]


    lista_esq = merge_sort(lista_esq)
    lista_dir = merge_sort(lista_dir)

    pos_esq = 0
    pos_dir = 0
    ordenada = []

    while pos_esq < len(lista_esq) and pos_dir < len(lista_dir):
        if lista_esq[pos_esq] < lista_dir[pos_dir]:
            ordenada.append(lista_esq[pos_esq])
            pos_esq += 1
        else:
            ordenada.append(lista_dir[pos_dir])
            pos_dir += 1

    
    sobra = None 

    if (pos_esq < pos_dir):
        sobra = lista_esq[pos_esq:] 
    else: 
        sobra = lista_dir[pos_dir:]
        
    
    return ordenada + sobra

##############################################
from data.emp10mil import empresas10
from data.emp25mil import empresas25
from data.emp50mil import empresas50
from data.emp100mil import empresas100
from time import time
import tracemalloc


#10mil
ini=time()
tracemalloc.start()

nomes_ord = merge_sort(empresas10)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim=time()

#print(nomes_ord)
print("10 mil")
print(f"Tempo: {fim-ini}")
print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

tracemalloc.stop()

#25mil
ini=time()
tracemalloc.start()

nomes_ord = merge_sort(empresas25)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim=time()

#print(nomes_ord)
print("25 mil")
print(f"Tempo: {fim-ini}")
print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

tracemalloc.stop()

#50mil
ini=time()
tracemalloc.start()

nomes_ord = merge_sort(empresas50)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim=time()

#print(nomes_ord)
print("50 mil")
print(f"Tempo: {fim-ini}")
print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

tracemalloc.stop()

#100mil
ini=time()
tracemalloc.start()

nomes_ord = merge_sort(empresas100)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim=time()

#print(nomes_ord)
print("100 mil")
print(f"Tempo: {fim-ini}")
print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

tracemalloc.stop()