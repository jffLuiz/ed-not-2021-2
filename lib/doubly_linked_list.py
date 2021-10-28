"""    
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA    - A lista encadeada é uma estrutura de dados formada por unidades      de informação chamadas nodos ou nós.    - Cada nodo da lista encadeada tem três partes: uma, que armazena a      informação; a segunda, que guarda o endereço do nodo anterior; e a      terceira, que guarda o endereço para o nodo seguinte da sequência    - A qualquer momento, temos um conhecimento apenas limitado de onde      se encontram todos os nodos da lista. Sabemos apenas onde está o      primeiro e o último nodo da sequência. Os nodos intermediários precisam      ser encontrados partindo-se do primeiro OU do último nodo e percorrendo      a sequência
"""

'''
    classe que representa cada unidade (elemento) da lista encadeada. é dividida em tres partes:
    1- o ponteiro para o nodo anterior da sequencia (prev)
    2- onde fica armazenada a informação relevante para o usuario (data)
    3- o ponteiro para o proximo nodo da sequencia (next)
'''

import math

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
        metodo que retorna o numero de nodos da lista
    """
    def count(self):
        return self.__count
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
        metodo que encontra a posição de um nodo, dado o seu valor
    """
    def index(self, pos):
        #encontra a posição do meio da lista, se o resultado for fracionario, considera o proximo numero inteiro
        meio = math.ceil(self.count / 2)

        #inicializa dois nodos, um com a cabeça e outro com a cauda da lista
        node1 = self.__head
        node2 = self.__tail

        #contador que vai até a metade da lista
        for i in range(0, meio + 1):
            if(node1.data == pos): return i #retorna a posição encontrada
            if(node2.data == pos): return self.__count -1 -i #retorna posição retroativa
            node1 = node1.next #node1 anda para frente
            node2 = node2.prev #node2 anda para tras

        return -1 #não encontrou o valor da lista

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
        método de atalho para inserção no inicio da lista
    """
    def insert_head(self, val):
        self.insert(0, val)

    """
        metodo de atalho para inserção no final da lista
    """
    def insert_tail(self, val):
        self.insert(self.__count, val)

    """
        metodo para remoção em qualquer posição
    """
    def remove(self, pos):
        """
            1°caso: lista vazia ou posição fora dos limites
        """
        if self.is_empty() or pos < 0 or pos > self.__count -1: return None
        """
            2°caso: remoção do inicio da lista
        """
        if pos == 0:
            #será removido o __head da lista
            removed = self.__head
            # o novo __head passa a ser o nodo seguinte ao removido
            self.__head = removed.next
            #se __head for um novo valido, ele nao pode ter um antecessor (prev)
            if self.__head is not None: self.__head.prev = None
            # em caso de remoção do unico nodo restante, __head é None, e __tail precisa ser None tbm
            if self.__count == 1: self.__tail = None

        #3° caso: remoção do ultimo nodo
        elif pos == self.__count -1:
            #será removido o __tail da lista
            removed = self.__tail
            #o novo __tail passa a ser o nodo anterior ao removido
            self.__tail = removed.prev
            #se __tail for um novo valido, ele não pode ter sucessor (next)
            if self.__tail is not None: self.__tail.next = None
            # em caso de remoção do unico nodo restante, __tail é None, e __head precisa ser None tbm
            if self.__count == 1: self.__head = None
        
        #4°caso: remoção de posição intermediario
        else: 
            #manda rencontar o nodo a ser removido
            removed = self.__find_node(pos)
            before = removed.prev
            after = removed.next
            # o nodo before passa a apontar a frente para o nodo after
            before.next = after
            #o nodo after passa a apontar para tras para o nodo before
            after.prev = before

        self.__count -= 1

        return removed.data

    
    """
        metodo de atalho para remoção na primeira posição
    """
    def remove_head(self):
        return self.remove(0)
    """
        metodo de atalho para remoção na ultima posição
    """
    def remove_tail(self):
        return self.remove(self.__count - 1)

    """
        metodo para consultar qualquer nodo, dada sua posição
    """
    def peek(self, pos):
        #lista vazia ou posições fora dos limites
        if self.is_empty() or pos < 0 or pos > self.__count -1: return None
        node = self.__find_node(pos)
        return node.data

    """
        metodo de atalho para consultar o primeiro nodo
    """
    def peek_head(self):
        return self.peek(0)

    """
        metodo de atalho para consultar o ultimo nodo
    """
    def peek_tail(self):
        return self.peek(self.__count - 1)


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

#remoção do primeiro nodo
removido = lista.remove(0)
print(f"Removido primeira posição: {removido}")
print(lista.to_str())

#remoção do ultimo nodo
removido = lista.remove(lista.count() - 1)
print(f"Removido ultima posição: {removido}")
print(lista.to_str())

#remoção de posição intermediaria
removido = lista.remove(2)
print(f"Removido posição 2: {removido}")
print(lista.to_str())

#consulta o ultimo nodo
ultimo = lista.peek_tail()
print(f"ultimo nodo consultado: {ultimo}")
print(lista.to_str())

