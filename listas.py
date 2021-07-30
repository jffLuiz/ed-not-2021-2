# criando uma lista (vetor)
primos = [2,3,5,7,11,13,17,19,23,29]

'''# percurso 
for num in primos:
    print(num)'''
print(primos)

# Acrescentar um novo elemento no FIM da lista: append()
primos.append(31)

print(primos)

# inserindo um elemento em uma posição especifica: insert()
# 1º -> informa a posição de inserção
# 2º -> elemento a ser inserido
primos.insert(0,1)

print(primos)

# insere o valor 37 na posição 5
primos.insert(5,37)

print(primos)

# removendo o ultimo elemento da lista: pop()
ultimo=primos.pop() # .pop() -> pode ser usado e apenas retira o ultimo elemento
print(f'ultimo: {ultimo}')
print(primos)

# removendo por valor: remove()
primos.remove(37)
print(primos)

# removendo por posição: del()
# removendo o elemento da posição 4
del primos[4]
print(primos)

# fatiando uma lista
# exibindo apenas o elemento da posição 0 (inclusive) a posição 7 (exclusive)
print(primos[0:7])

# da posição 2 a posição 8 
print(primos[2:8])

# fatiando e criando uma sublista
subPrimos=primos[1:5]
print(subPrimos)