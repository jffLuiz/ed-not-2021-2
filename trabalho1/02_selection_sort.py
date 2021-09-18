
def selection_sort(lista):
    '''função que implementa o algoritmo de ordenação selection sort'''
    for pos_sel in range(len(lista)-1):
        pos_menor=pos_sel+1
        for j in range(pos_sel+2, len(lista)):
            if lista[j] < lista[pos_menor]:
                pos_menor=j

        if lista[pos_menor] < lista [pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]

####################################################

from data.emp10mil import empresas10
from data.emp25mil import empresas25
from data.emp50mil import empresas50
from data.emp100mil import empresas100
from time import time
import tracemalloc


#10mil
ini=time()
tracemalloc.start()

nomes_ord = selection_sort(empresas10)

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

nomes_ord = selection_sort(empresas25)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim=time()

#print(nomes_ord)
print("25 mil")
print(f"Tempo: {fim-ini}")
print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

tracemalloc.stop()

# #50mil
# ini=time()
# tracemalloc.start()

# nomes_ord = selection_sort(empresas50)

# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# fim=time()

# #print(nomes_ord)
# print("50 mil")
# print(f"Tempo: {fim-ini}")
# print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

# tracemalloc.stop()

# #100mil
# ini=time()
# tracemalloc.start()

# nomes_ord = selection_sort(empresas100)

# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# fim=time()

# #print(nomes_ord)
# print("100 mil")
# print(f"Tempo: {fim-ini}")
# print(f'pico de memoria: {mem_pico / 1024 / 1024}mb')

# tracemalloc.stop()