def quick_sort(lista, ini=0, fim=None):
    '''
        funcao que complementa o algoritmo de ordenação quick sort de forma recursiva
    ''' 
    if fim is None:
        fim = len(lista)-1

    if fim <= ini:
        return  

    pivot = fim 
    div = ini -1   

    for i in range(ini, fim):
        if lista[i] < lista[pivot]:
            div+=1 
            if div != i: 
                lista[div], lista[i] = lista[i], lista[div]
    
    div += 1

    if lista[pivot] < lista[div] and pivot != div:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        

    quick_sort(lista, ini, div-1)

    quick_sort(lista, div + 1, fim)

####################################

from data.emp10mil import empresas10
from data.emp25mil import empresas25
from data.emp50mil import empresas50
from data.emp100mil import empresas100
from time import time
import tracemalloc


#10mil
ini=time()
tracemalloc.start()

nomes_ord = quick_sort(empresas10)

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

nomes_ord = quick_sort(empresas25)

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

nomes_ord = quick_sort(empresas50)

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

nomes_ord = quick_sort(empresas100)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim=time()

#print(nomes_ord)
print("100 mil")
print(f"Tempo: {fim-ini}")
print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

tracemalloc.stop()