# print() exibe informações
print('Hello World!!!')

# input() permite a entrada de informações
nome=input('qual é seu nome? ')

print(f'olá, {nome}')

#int() converte o que foi informado no input() de texto para numero inteiro
idade=int(input('informe sua idade: ')) 

if idade >=18:
    print('vc ja pode beber.')
    print('vc ja pode tirar habilitação')
else:
    print('vc não pode beber')
    print('vc não pode dirigir')