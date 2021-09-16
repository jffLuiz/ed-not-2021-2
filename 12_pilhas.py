#palindromo: é um texto que, quando lido de tras para frente, mantes o mesmo conteudo (desprezando acentos e espaçamento)
#texto = "socorram-me, subi no onibus em marrocos"

texto = "batatinha quando nasce espalha rama pelo chao"

pilha = []

#percurso do palindromo, colocando cada letra na lista
for letra in range(len(texto)):
    pilha.append(texto[letra]) #append() sempre acrescenta por ultimo

# pilha.insert(10, 'y')
# pilha.insert(19, 'g')
# pilha.insert(6, 'ç')


print(pilha)

#remoção de elementos em posição que não são o final
# del pilha[11] #remove a posição 11
# del pilha[21] #remove a posição 21
# del pilha[8]
# del pilha[25] 

inverso = ""

#retira cada letra da lista, de tras para frente, e coloca no inverso
while len(pilha)>0:
    inverso += pilha.pop() #pop() retira sempre o ultimo elemente

print(inverso)


# PILHA
#a pilha é um tipo de abstrato de dados (TAD) que permite a entrada e a saida de dados apenas na sua extremidade final. Como consequencia, ela segue a regra LIFO (last in, first out - ultimo a entrar, primeiro a sair) e tem acesso limitado aos seus elementos.
