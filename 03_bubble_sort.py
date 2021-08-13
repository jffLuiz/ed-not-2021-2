# algoritmo de ordenação bubble sort
#percorre a lista a ser ordenada em sucessivas passadas, trocando elemento adjacentes entre si quando o segundo for menor que o primeiro. efetua tantas passadas quanto necessarias, até que, na ultima passada, nenhuma troca seja efetuada.

def bubble_sort(lista):
    '''função que implementa o algoritmo de ordenação bubble sort '''
    while True: #loop eterno
        trocou = False
        #loop na lista até o penultimo elemento: len(lista) - 2
        #ex: em uma lista de 10 elementos, len(lista) == 10 ... a ultima posição estará em len(lista) -1, ou seja 9 ... a penuntima posição estará em len(lista) - 2, ou seja, 8.
        for i in range(len(lista)-2): #inicia nova passada
            if lista[i+1] < lista[i]: #é necessario trocar
                lista[i+1], lista[i] = lista[i], lista[i+1] #faz a troca
                trocou=True
        #se não houve troca, a lista esta ordenada e podemos interromper o loop while
        if not trocou: #trocou == false
            break # interrompe o while
