#funcao  é um trecho de código que tem um nome e pode receber informações externas para fazer seu trabalho. opcionalmente uma funcao pode tbm produzir um valor de resultado. Uma funcao é definida apenas uma vez e pode ser utilizada (chamada) varias vezes, evitando repetições no código.
#existem funcoes ja providas pela linguagem (funcoes internas), como por exemplo len(), range() e sort(), e podemos definir tbm nossas proprias funcoes.

#os termos que aparecem entre parenteses são chamados de parametros ou argumentos
def imc(peso, altura): #definiçaõ (ou declaração) da funcao
    """
        funcao que calcula o indice de massa corporal (imc)
    """
    #trechos entre aspas tripas são um tipo especial de comentario chamado docstring, e servem para documentar o propósito de uma funcao ou classe
    return peso/(altura**2)

# float(): converte o valor informado em um numero com casas decimais (floating point)
p = float(input('informe o peso da pessoa: '))
a = float(input('informe a altura da pessoa: '))

#fazendo uma chama a funcao imc()
resultado = imc(p,a)
print(f'o imc é de {resultado}')