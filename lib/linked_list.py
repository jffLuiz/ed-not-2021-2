'''
    classe que representa cada unidade (elemento da lista encadeada). é dividida em duas partes:
    1- onde fica armazenada a informação relevante para o usuario (data)
    2- o ponteiro para o proximo nodo da sequencia (next)
'''

class Node:

    def __init__(self, val):
        self.data = val #armazena a informação do usuario
        self.next = None #ponteiro para o proximo node (None = Nenhum)



'''
    ESTRUTURA DE DADOS LISTA ENCADEADA
    - A lista encadeada é uma estrutura de dados formada por unidades      de informação chamadas nodos ou nós.
    - Cada nodo da lista encadeada tem duas partes: uma, que armazena a      informação e outra que guarda o endereço do próximo nodo da sequência
    - A qualquer momento, temos um conhecimento apenas limitado de onde      se encontram todos os nodos da lista. Sabemos apenas onde está o      primeiro e o último nodo da sequência. Os nodos intermediários precisam      ser encontrados partindo-se do primeiro e percorrendo a sequência
'''


class LinkedList: 
    
    '''
        Construtor da classe
    '''
    def __init__(self):
        self.__head = None # ( cabeça ) ponteiro para o primeiro nodo da lista
        self.__tail = None # ( calda ) ponteiro para o ultimo nodo da lista
        self.__count = 0 #contador de nodos
    
    """
        método que informa se a lista esta ou não vazia
    """
    def is_empty(self):
        return self.__count == 0

    def insert(self, pos, val):

        inserted = Node(val)

        #1ºCASO: lista esta vazia
        # o node criado será, ao mesmo tempo, o primeiro e o ultimo
        if self.is_empty():
            self.__head = inserted
            self.__tail = inserted


        #2ºCASO: inserção no inicio da lista (posição 0)
        elif pos == 0 :
            inserted.next = self.__head
            self.__head = inserted
        
        #3ºCASO: inserção no fim da lista 
        #vamos considerar qualquer posição de inserção >= count como inserção no final
        elif pos >= self.__count:
            self.__tail.next = inserted
            self.__tail = inserted 

        #4ºCASO: inserção em posição intermediaria
        else:
            before = self.__head

            #percorre a lista encadeada até a posição anterior aquela da inserção
            for i in range(1, pos): 
                print(f"before.data: {before.data}, i: {i}")
                before = before.next 


        self.__count += 1

        #print(f"[NODE] data: {inserted.data}, next: {inserted.next}")

#########################################################

lista = LinkedList()

lista.insert(0, "1kg batata")
lista.insert(1, "café")
lista.insert(2, "miojo")
lista.insert(3, "oleo")
lista.insert(4, "sabonete")
lista.insert(5, "shampoo")

lista.insert(4, "papel")



