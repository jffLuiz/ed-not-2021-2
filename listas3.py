#lista de strings
frutas = ["laranja","maça","uva","pera","mamao","abacate","amora"]
print(frutas)
print ('------------')

#imprimindo apenas a fruta uva
print(frutas[2])

print ('------------')

#substituindo "pera" por "melao"
frutas[3]="melao"

print(frutas)
print ('------------')

#descobrindo quantos elementos ha na lista
print(len(frutas))
print ('------------')

#percorrendo e imprimindo cada um dos elementos da lista
for fruta in frutas:
    print(fruta)
print ('------------')

#percorrendo e imprimindo cada elemento e sua posição
for i in range(len(frutas)):
    print(f"{frutas[i]} esta na posição {i}")
print ('------------')

# percurso em ordem invertida
# 1ºargumento: len(frutas)-1 : a lista precisa começar no ultimo elemento, que é determinado por len()-1
# 2º argumento: -1, pq o limite final não entre e precisamos terminar em 0
# 3º argumento: -1, pq a lista precisa ser decrescente
for j in range(len(frutas)-1, -1, -1):
    print(frutas[j])

print ('------------')

# ordenando a lista em ordem alfabetica
frutas.sort() #altera tbm a ordem na lista
print(frutas)
for i in range(len(frutas)):
    print(f"{frutas[i]} esta na posição {i}")
print ('------------')