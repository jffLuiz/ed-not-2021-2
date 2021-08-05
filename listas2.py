# range(): gera uma faixa de numeros

#range() com 1 argumento: gera uma lista de numeros que vai de 0 até argumento -1

for i in range(10):
    print (i)

print ('------------')

#range() com dois argumentos: gera uma lista de numeros começando pelo primeiro argumento (inclusive) até o segundo argumento (exclusive)
for j in range(5,15):
    print(j)


print ('------------')
#range() com tres argumentos: 1- limite inferior(inclusive); 2- limite superior (exclusive); 3- passo(de quanto em quanto a lista ira andar)
for k in range(1, 22, 3):
    print(k)

print ('------------')

for n in range(10, 0, -1):
    print(n)