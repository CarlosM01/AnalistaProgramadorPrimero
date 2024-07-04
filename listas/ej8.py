# 8. Escriba un programa que almacene automáticamente en una lista los números del 1 al 50, muestre en
# pantalla la lista, luego elimine de la lista los números que ocupen posiciones (índices) múltiplos de 3, y
# muestre por pantalla la lista resultante.

lista = []

for i in range(1,51):
    lista.append(i)

print(lista)

i = 0
while i < len(lista):
    del lista[i]
    i += 2

print(lista)
