from lib.linked_list import LinkedList

lista = LinkedList()

lista.insert(0, "1kg batata")
lista.insert(1, "café")
lista.insert(2, "miojo")
lista.insert(3, "oleo")
lista.insert(4, "sabonete")
lista.insert(5, "shampoo")

lista.insert(4, "papel")

lista.insert(7, "sabão em pó")
lista.insert(30, "detergente")

#print(lista.to_str())

lista.insertFront("5kg arroz")
lista.insertBack("agua sanitaria")

print(lista.to_str())

print(f"info do nodo da posição 7: {lista.peek(7)}")
print(f"info do nodo da posição 7: {lista.peek(13)}")

print(f"posição de tomate: {lista.index('tomate')}")
print(f"posição de café: {lista.index('café')}")
print(f"posição de cebola: {lista.index('cebola')}")


print('-----------------------------------')

print(lista.to_str())

#remoção do inicio da lista
removido = lista.remove(0)


print(f"valor removido: {removido}")
print(lista.to_str())

#remoção da posição 5
removido = lista.remove(5)

print(f"valor removido da posição 5: {removido}")
print(lista.to_str())


#remoção do ultimo nodo
removido = lista.remove(lista.count()-1)

print(f"valor removido do ultimo nodo: {removido}")
print(lista.to_str())

#remoção do ultimo nodo (usando removeTail())
removido = lista.removeTail()

print(f"valor removido do ultimo nodo: {removido}")
print(lista.to_str())

