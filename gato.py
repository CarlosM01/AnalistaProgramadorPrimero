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
            print('Utilice una opción válida')

def select_side():        
    while True:
        side = (input('''
    Establecer el número de casillas por lado
    deben el tablero debe ser de al menos 3x3
    '''))
        
        if (side.isdigit() and int(side) >= 3):
            return int(side)


def show_table(select=False, side=3):  
    tableObj = []
    table = []        
    for r in range(1,side+1):
        
        objCol = []
        objRow = []
        cols = []
        rows = [] 
        for c in range(1,side+1):
            
            # squareOj = {"posX": r, "posY": c, "figure": "_"}
            squareOj = {"figure": "_"}
            objCol.append(squareOj)

            square = ''
            square += str(r)
            square += str(c)
            if (select): 
                square = f'_{square}_'
            else: square = f'___'
            cols.append(square)

        
        #objRow.append(objCol)
        rows.append(cols)
        rowStr = str(rows)
        print (rowStr.replace('[', '').replace(']', '').replace(',', '|').replace("'", '').replace(' ', ''))
        table.append(cols)
        tableObj.append(objCol)
        

    print(table)
    print(table[1][1])
    print(tableObj[1][1])


    



def choose_square():
    while True:
        eleccion =  input('Selccione casilla')

        print('_1_|_2_|_3_')
        print('_4_|_5_|_6_')
        print('_7_|_8_|_9_')


    

elegir_figura()
create_table(select=True)
        
    