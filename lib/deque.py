class Deque: 
    '''
        ESTUTURA DE DADOS DEQUE  - Deque = Double-Ended Queue (fila de duas pontas)  - Deque é uma lista linear de acesso restrito, que permite apenas as operações  de enfileiramento (insert_front/insert_back) e desenfileiramento  (remove_front/remove_back), acontecendo em qualquer uma das extremidades da estrutura.  - Como consequência, o deque NÃO SEGUE o princípio FIFO (First In, First Out - primeiro a entrar, primeiro a sair).  - A principal aplicação dos deques são situações em que filas precisam aceitar  a inserção de itens prioritários e a desistência do último item.
    '''


    '''
        construtor de classe
    '''
    def __init__(self):
        self.__data = [] #inicializa uma lista privada vazia

    '''
        método para inserção no inicio do deque
    '''
    def insert_front(self, val):
        self.__data.insert(0, val)
    
    '''
        método para inserção no final do deque
    '''
    def insert_back(self, val):
        self.__data.append(val)
    '''
        método para remoção no inicio do deque
    '''
    def remove_front(self):
        if self.is_empty(): return None
        return self.__data.pop(0)
    '''
        método para remoção no final do deque
    '''
    def remove_back(self):
        if self.is_empty(): return None
        return self.__data.pop()
    '''
        método para consulta o inicio do deque (primeiro elemento), sem retira-lo
    '''
    def peek_front(self):
        if self.is_empty(): return None
        return self.__data[0]
    '''
        método para consulta o final do deque (ultimo elemento), sem retira-lo
    '''
    def peek_back(self):
        if self.is_empty(): return None
        return self.__data[-1]

    """
        método para verificar se o deque esta vazia ou não
        retorne true se vazia ou false caso contrário
    """
    def is_empty(self):
        return len(self.__data) == 0

    """
        método que exibe o deque como um string (para fins de depuração)
    """ 
    def to_str(self):
        string = ""
        for el in self.__data:
            if string != "": string += ", "
            string += str(el)
        return "[ " + string + " ]"
#############################################

