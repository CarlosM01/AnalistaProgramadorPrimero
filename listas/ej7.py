# 7. Escriba un programa que almacene automáticamente en una lista los números del 1 al 50, muestre en
# pantalla la lista, luego elimine de la lista los números múltiplos de 3, y muestre por pantalla la lista
# resultante.

lista = []

for i in range(1,51):
    lista.append(i)

print(lista)

for i  in lista:
    if i%3 == 0:
        lista.remove(i)

print(lista)