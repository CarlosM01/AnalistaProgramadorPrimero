print('Bienvenid@ al gato en python')

def elegir_figura():
    print('Jugador 1 escoja entre X y O')
    print(''' 
Escribe 1 para elegir X
Escribe 2 para elegir O
''')
    while True:
        jug_elec = input('Seleccione opcion')
        if (jug_elec == '1'):
            print('elegiste X')
            return 'X' 
        elif (jug_elec == '2'):
            print('elegiste O')
            return 'O'
        else:
            print('Por favor no sea weon')

n = elegir_figura()


def mostrar_tablero():
    c1 = c2 = c3 = c4 = c5 = c6= c7 = c8 = c9 = '_'

    print(f'_{c1}_|_{c2}_|_{c3}_')
    print(f'_{c4}_|_{c5}_|_{c6}_')
    print(f'_{c7}_|_{c8}_|_{c9}_')

mostrar_tablero()

def escoger_casilla():
    while True:
        eleccion =  input('Selccione casilla')

        print('_1_|_2_|_3_')
        print('_4_|_5_|_3_')
        print('_1_|_2_|_3_')

    