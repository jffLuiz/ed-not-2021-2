from lib.doubly_linked_list import DoublyLinkedList


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
lista.insert(1, 'gol')
print(lista.to_str())

#inserção em posição intermediaria
lista.insert(4, 'corcel')
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

# inserçoes adicionais no final da lista
lista.insert_tail('passat')
lista.insert_tail('fiorino')
lista.insert_tail('variant')
lista.insert_tail('escort')
lista.insert_tail('del ray')
print(lista.to_str())


idxCorcel = lista.index('corcel')
idxVariant = lista.index('variant')
idxEscort = lista.index('escort')
idxGol = lista.index('gol')
idxChevette = lista.index('chevette')
idxPassat = lista.index('passat')

print(f"posições: corcel: {idxCorcel}; variant: {idxVariant}; escort: {idxEscort}; gol: {idxGol}; chevette: {idxChevette}; passat: {idxPassat}")