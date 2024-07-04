# 12. Escriba un programa que permita almacenar el nombre de 5 frutas, luego cree una nueva lista con el
# largo de cada palabra registrada. Ej. Usuario ingresa manzana, pera, mango -> lista2=[“7”,”4”,”5”]

wordsList = []
wordsLen = []

for i in range(5):
    while True:
        word = input('Ingrese una palabra')
        if word.isalpha():
            word = word.strip()
            break
        else: print('No debe contener numeros ni digitos especiales')

    wordsList.append(word)
    length = len(word)
    wordsLen.append(length)

print(wordsList)
print(wordsLen)


    
