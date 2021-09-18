def bubble_sort(lista):
    '''função que implementa o algoritmo de ordenação bubble sort '''

    while True: 
        trocou = False
        for i in range(len(lista)-1): 
            if lista[i+1] < lista[i]: 
                lista[i+1], lista[i] = lista[i], lista[i+1] 
                trocou=True
        if not trocou: 
            break 

#####################################################################

from data.emp10mil import empresas10
from data.emp25mil import empresas25
from data.emp50mil import empresas50
from data.emp100mil import empresas100
from time import time
import tracemalloc


#10mil
ini=time()
tracemalloc.start()

nomes_ord = bubble_sort(empresas10)

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

nomes_ord = bubble_sort(empresas25)

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

nomes_ord = bubble_sort(empresas50)

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

nomes_ord = bubble_sort(empresas100)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim=time()

#print(nomes_ord)
print("100 mil")
print(f"Tempo: {fim-ini}")
print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

tracemalloc.stop()


