"""
    Analisador de expressoes matematicas
"""

from lib.stack import Stack

simbolos = {
        "P" : "parêntese",
        "C" : "colchete",
        "X" : "chave"
}

expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1] * 3} / 5"
#expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1} * 3] / 5"
#expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1]] * 3} / 5"
#expressao = "2 * {4 - {7 / [(5 - (7 * 9) + 1] * 3} / 5"

analisador = Stack() #cria a pilha

def verif_fechamento(tipo_fecha, pos_fecha, dados_abre):
    # se o tipo que veio da pilha for igual ao tipo encontrado no fechamento, OK
    #print(f"DEBUG -> tipo_fecha: {tipo_fecha}, pos_fecha: {pos_fecha}, dados_abre: {dados_abre}")

    #a pilha ficou vazia antes do termino da analise da expressão
    if dados_abre is None: 
        print(f"ERRO: ha mais simbolos de fechamento que simbolos de abertura na expressao; tipo: {tipo_fecha}, posição {pos_fecha}")
    elif dados_abre["tipo"] == tipo_fecha:
        print(f"Simbolo {tipo_fecha} aberto na posição {dados_abre['pos']} e fechando na posição {pos_fecha}")
    else: #tipos errados
        print(f"ERRO: simbolo de fechamento do tipo {tipo_fecha} encontrado na posição {pos_fecha}; esperado simbolo do tipo {dados_abre['tipo']}")


#percorre a expressao em busca de parenteses, colchetes e chaves
for pos in range(len(expressao)):
    if expressao[pos] == "(":
        #empilha informações sobre o abre parenteses
        analisador.push({"tipo": "P", "pos": pos})
    elif expressao[pos] == "[":
        #empilha informações sobre o abre colchetes
        analisador.push({"tipo": "C", "pos": pos})
    elif expressao[pos] == "{":
        #empilha informações sobre o abre chaves
        analisador.push({"tipo": "X", "pos": pos})
    elif expressao[pos] == ")":
        verif_fechamento("P", pos, analisador.pop())
    elif expressao[pos] == "]":
        verif_fechamento("C", pos, analisador.pop())
    elif expressao[pos] == "}":
        verif_fechamento("X", pos, analisador.pop())

#verificado se houve sobra(s) na pilha
while not analisador.is_empty():
    sobra = analisador.pop()
    print=(f"ERRO: simbolo de abertura {sobra['tipo']} sem simbolo de fechamento correspondente na posição {sobra['pos']}")
