from lib.deque import Deque

deque = Deque()  #cria um deque vazio
print(deque.to_str())

#inserções "normais"
deque.insert_back("tertuliano")
deque.insert_back("castorina")
deque.insert_back("astolfo")
deque.insert_back("wesclerson")
deque.insert_back("gilvanete")

print(deque.to_str())

#inserções prioritarias
deque.insert_front("hermogenes")
deque.insert_front("querencia")

print(deque.to_str())

#remoçoes "normais"
atendido = deque.remove_front()
print(f"atendido: {atendido}")
print(deque.to_str())

atendido = deque.remove_front()
print(f"atendido: {atendido}")
print(deque.to_str())

#desistencias (remoção no final)
desistente = deque.remove_back()
print(f"desistente: {desistente}")
print(deque.to_str())

desistente = deque.remove_back()
print(f"desistente: {desistente}")
print(deque.to_str())

#consultando as extremidades do deque
primeiro = deque.peek_front()
ultimo = deque.peek_back()
print(f"primeiro: {primeiro}. ultimo: {ultimo}")
print(deque.to_str())