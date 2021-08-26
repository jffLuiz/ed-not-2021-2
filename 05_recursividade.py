# fatorial de um numero n 
# é igual ao numero n multiplicado por todos seu antecessores até 1

# 7! = 7*6*5*4*3*2*1 = 5040
# 6! = 6*5*4*3*2*1 = 720
# 5! = 5*4*3*2*1 = 120
# 4! = 4*3*2*1 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# 1! = 1
# 0! = 1 (por convensão)

# 5! = 5*4!
# 4! = 4*3!
# 3! = 3*2!
# 2! = 2*1!
# 1! = 1*0!

# n! = n*(n-1)! p/ n>1

# implementação iterativa (iter = caminho)
def fatorial (n):
    resultado=1
    if(n>1):
        #range começa no numero n e vai decrescendo até 1
        for i in range(n, 1, -1):
            resultado*=i
            print(f'Resultado: {resultado}, i: {i}')
    return resultado

print(f'5! = {fatorial(5)}')
print(f'7! = {fatorial(7)}')

# n! = n*(n-1)! p/ n>1
# recursividade ocorre quando a definição de um função inclui a própria função sendo definida 

# em programação, a recursividade se traduz quando uma função efetua chamadas a si própria.

print('--------------------')
# implementação recursiva
def fatorial2(n):
    # em uma função recursiva, a condeição de saida é aquela em que a função é capaz de retornar resultado sem chamar novamente a si mesma
    if n <= 1: #condição de saida
        return 1
    return n * fatorial2(n-1)

print(f'5! = {fatorial2(5)}')



