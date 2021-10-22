"""    
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA    - A lista encadeada é uma estrutura de dados formada por unidades      de informação chamadas nodos ou nós.    - Cada nodo da lista encadeada tem três partes: uma, que armazena a      informação; a segunda, que guarda o endereço do nodo anterior; e a      terceira, que guarda o endereço para o nodo seguinte da sequência    - A qualquer momento, temos um conhecimento apenas limitado de onde      se encontram todos os nodos da lista. Sabemos apenas onde está o      primeiro e o último nodo da sequência. Os nodos intermediários precisam      ser encontrados partindo-se do primeiro OU do último nodo e percorrendo      a sequência
"""

'''
    classe que representa cada unidade (elemento) da lista encadeada. é dividida em tres partes:
    1- o ponteiro para o nodo anterior da sequencia (prev)
    2- onde fica armazenada a informação relevante para o usuario (data)
    3- o ponteiro para o proximo nodo da sequencia (next)
'''

class Node:
    def __init__(self, val): 
        self.prev = None #ponteiro para o nodo anterior (None=nenhum)
        self.data = val #armazena a informação do usuario
        self.next = None #ponteiro para o proximo nodo (None = nenhum)

'''
    ESTRUTURA DE DADOS LISTA ENCADEADA
    - A lista encadeada é uma estrutura de dados formada por unidades      de informação chamadas nodos ou nós.
    - Cada nodo da lista encadeada tem duas partes: uma, que armazena a      informação e outra que guarda o endereço do próximo nodo da sequência
    - A qualquer momento, temos um conhecimento apenas limitado de onde      se encontram todos os nodos da lista. Sabemos apenas onde está o      primeiro e o último nodo da sequência. Os nodos intermediários precisam      ser encontrados partindo-se do primeiro e percorrendo a sequência
'''

class DoublyLinkedList: 
    """
        Construtor da classe
    """
    def __init__(self):
        self.__head = None # (cabeça) aponta para o inicio da lista
        self.__tail = None # (cauda) aponta para o fim da lista
        self.__count = 0 #contador de nodos

    """
        metodo que informa se a lista esta ou não vazia
    """
    def is_empty(self):
        return self.__count == 0

    """
        metodo privado que encontra um nodo, data a sua posição
    """
    def __find_node(self, pos):
        #encontra o nodo fazendo o percurso a partir de __head, se ele estiver na primeira metade da lista
        if pos < self.__count // 2:
            node = self.__head
            for i in range(1, pos + 1): node = node.next
        
        #se, ao contrario, o nodo estiver na segunda metade da lista, compensa fazer um percurso reverso desde o __tail
        else:
            node = self.__tail
            for i in range(self.__count -2, pos-1 , -1): node = node.prev
        
        return node



    """
        metodo para inserção de um novo nodo na lista
    """
    def insert(self, pos, val):

        inserted = Node(val)

        #1ºcaso: lista vazia
        if self.is_empty():
            self.__head = inserted
            self.__tail = inserted

        #2ºcaso: inserção na posição inicial
        elif pos == 0:
            inserted.next = self.__head #aponta para o seguinte
            self.__head.prev = inserted #aponta para o anterior
            self.__head = inserted #ajusta o inicio da lista
        
        #3ºcaso: inserção na posição final
        elif pos >= self.__count:
            inserted.prev = self.__tail
            self.__tail.next = inserted    
            self.__tail = inserted 
        
        #4ºcaso: inserção na posição intermediaria
        else:
            node_pos = self.__find_node(pos)
            before = node_pos.prev

            before.next = inserted
            inserted.prev = before
            inserted.next = node_pos
            node_pos.prev = inserted


        self.__count += 1    

    """
        método que exibe a pilha como um string (para fins de depuração)
    """ 
    def to_str(self):
        string = ""
        node = self.__head
        for i in range(0, self.__count):
            if string != "": string += ", "
            string += f"(pos: {i}, data: {node.data})"
            node = node.next
        return "[ " + string + f" ], count: {self.__count}"

###################################
lista = DoublyLinkedList()
print(lista.to_str())

#inserção em lista vazia
lista.insert(0, 'fusca')
print(lista.to_str())

#inserção no inicio da lista
lista.insert(0, 'chevette')
print(lista.to_str())

#inserção no final da lista
lista.insert(3, 'maverick')
print(lista.to_str())

#inserção no final da lista (2)
lista.insert(4, 'opala')
print(lista.to_str())

#inserção no final da lista (3)
lista.insert(5, 'del rey')
print(lista.to_str())

#inserção em posição intermediaria
lista.insert(1, 'Gol')
print(lista.to_str())

#inserção em posição intermediaria
lista.insert(4, 'Corcel')
print(lista.to_str())