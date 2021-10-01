from lib.queue import Queue

fila = Queue() #cria uma nova fila
print(fila.to_str())

#adicionando pessoas a fila
fila.enqueue("Marciovaldo")
fila.enqueue("Gildanete")
fila.enqueue("Terencionildo")
fila.enqueue("Junislerton")
fila.enqueue("Ritielaine")

print(fila.to_str())

atendido = fila.dequeue()
print(f"Atendido: {atendido}")
print(fila.to_str())

atendido = fila.dequeue()
print(f"Atendido: {atendido}")
print(fila.to_str())

fila.enqueue("Adenoirton")
print(fila.to_str())

proximo = fila.peek()
print(f"Proximo a ser atendido: {proximo}")
print(fila.to_str())
