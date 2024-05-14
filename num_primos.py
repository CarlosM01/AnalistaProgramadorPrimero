num = int(input('ingrese un numero'))

if num <= 1:
    result = 'No es primo'
else:
    result = 'Es primo'
    for i in range(2,num):
        if(num%i == 0):
            result = 'No es primo'
            break

print(result)