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
            
            #percorre a lista encadeada da segunda posição (pos. 1) até a posição anterior aquela da inserção
            for i in range(1, pos): before = before.next 
                
            #nodo de ficará dapois do inserido
            after = before.next

            #o next do nodo inserido passa a ser o after
            inserted.next = after

            #o next do nodo before passa a ser o inserted
            before.next = inserted

        self.__count += 1

    '''
        método de atalho para inserção na primeira posição
    '''
    def insertFront(self, val):
        self.insert(0, val)


    '''
        método de atalho para inserção na ultima posição
    '''
    def insertBack(self, val):
        self.insert(self.__count, val)

    '''
        retorna o data do nodo da posição especificada
    '''
    def peek(self, pos):
        #quando a lista estiver vazia ou a posição estiver fora dos limites validos (0 .. count -1), retorna None
        if self.is_empty() or pos < 0 or pos > self.__count - 1:
            return None
        node = self.__head
        for i in range(0, pos): node = node.next
        return node.data

    """
        método para procurar um valor na lsita e retornar sua posição. Retorna -1 caso não encontre.
    """
    def index(self, val):
        node = self.__head
        for pos in range(0, self.__count):
            if node.data == val: return pos
            node = node.next
        return -1 #não encontrou

    """
        método para remover um elemento da lista
    """
    def remove(self, pos):
        #1º caso: lista vazia ou posição fora dos limites(menor que 0 ou mais que count - 1)
        if self.__count == 0 or pos < 0 or pos > self.__count -1:
            return None

        #2ºcaso: remoção do inicio da lista
        if pos == 0:
            removed = self.__head  #nodo removido
            self.__head = self.__head.next #passa a apontar para o node seguinte

        #3ºcaso: remoções intermediarias ou finais
        else:
            #percore a lista até encontrar o item anterior a posição a remoção (before)
            before = self.__head
            for i in range(1, pos): before = before.next

            #o removido será o sucessor do before
            removed = before.next

            # nodo da posição seguinte à de remoção (next)
            after = removed.next

            #o nodo anterior (before) passa a apontar para o nodo seguinte (after) 
            before.next = after

            #atualizando o __tail no caso da remoção do ultimo nodo
            if removed == self.__tail:
                self.__tail = before



        self.__count -= 1
        #retorna o valor armazenado no nodo removido
        return removed.data 

    """
        método para remover o primeiro nodo da lista 
    """
    def removeHead(self):
        return self.remove(0)

    """
        método para remover o ultimo nodo da lista 
    """
    def removeTail(self):
        return self.remove(self.__count - 1)
   

    """
        método que retorna a quantidade de itens da lista
    """
    def count(self):
        return self.__count

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

        

#########################################################

