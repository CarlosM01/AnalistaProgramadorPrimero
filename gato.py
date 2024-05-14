print('Bienvenid@ al gato en python')


class player():
    def __init__(self):
        self.icon

    def select_icon(self):
        print('Jugador 1 escoja entre X y O')

        while True:
            jug_elec = input('Seleccione opcion:  ')
            if (jug_elec.upper() == 'X'):
                print('elegiste X')
                self.icon = 'X'
                break
            elif (jug_elec.upper() == 'O'):
                print('elegiste O')
                self.icon = 'O'
                break
            else:
                print('Utilice una opción válida')


class Square:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

        self.icon = ''
        self.icon += str(posX)
        self.icon += str(posY)

        self.id = int(self.icon) 
        self.iconMenu = f'_{self.icon}_'
        self.icon = '___'
        

class Table:
    def __init__(self):
        self.side = 3
        self.data = {}
        self.display = ''

    def setSide(self):        
        while True:
            side = (input('''
        Establecer el número de casillas por lado
        deben el tablero debe ser de al menos 3x3
        
                          -->  
        '''))
            
            if (side.isdigit() and int(side) >= 3):
                self.side = side
                break
        
    def generate(self):       
        for x in range(self.side):
            for y in range(self.side):
                sre = Square(x, y)                
                self.data[sre.id] = sre

    def showIcon(self):
        count = 1
        for i in self.data:
            self.display += self.data[i]

            if count % self.side == 0:
                self.display += "\n"
            count+= 1
        
        print(self.display)
    
    def chooseSquare(self):
        input('Elegir Casilla: ')
        

        
    