from os import system

print('Bienvenid@ al gato en python')


class Player():
    def __init__(self) -> None:
        pass

    def setName(self, num):
        name = input(f'Jugador {num}, ingrese su nombre:  ')
        name = name.capitalize()
        self.name = name

    def select(self):
        
        print(f'{self.name}, escoje entre X y O')

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
    def __init__(self, posX, posY, icon = '_'):
        self.posX = posX
        self.posY = posY
        self.icon = icon

        self.id = str(posX)
        self.id += str(posY)

        self.iconMenu = f'_{self.id}_'        
        

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

        '''))
            
            if (side.isdigit() and int(side) >= 3):
                self.side = int(side)
                break
        
    def generate(self):       
        for x in range(self.side):
            for y in range(self.side):
                sre = Square(x, y)                
                self.data[sre.id] = sre

    def showId(self):
        self.display = ''
        count = 1
        for i in self.data:
            if self.data[i].icon == '_':
                self.display += f'|_{self.data[i].id}_'
            else:
                self.display += f'|__{self.data[i].icon}_'
                
            if count % self.side == 0:
                self.display += "|\n"
            count+= 1
        
        system('clear')
        return print(self.display)


    def setSquare(self, player):
        icon = player.icon
        name = player.name
        while True:
            select = input(f'{name}, elige una casilla: ')
            if select in self.data:
                if self.data[select].icon == '_':
                    self.data[select].icon = icon
                    break
                else: print('Esa casilla ya está seleccionada')
            else: print('Fuera de rango')

    def winner(self):
        #Horizontales
        for x in range(self.side):
            pointsX = 0
            pointsO = 0
            for y in range(self.side):
                pos = str(x)+str(y)
                if self.data[pos].icon == 'X':
                    pointsX += 1
                if pointsX == 4:
                    return 'X'  
                if self.data[pos].icon == 'O':
                    pointsO += 1
                if pointsO == 4:
                    return 'Y'
        
        #Verticales
        for y in range(self.side):
            pointsX = 0
            pointsO = 0
            for x in range(self.side):
                pos = str(x)+str(y)
                if self.data[pos].icon == 'X':
                    pointsX += 1
                if pointsX == 4:
                    return 'X'  
                if self.data[pos].icon == 'O':
                    pointsO += 1
                if pointsO == 4:
                    return 'O'
        
        #Diagonal1
        pointsX = 0
        pointsO = 0
        for i in range(self.side):
            pos = str(i)*2
            if self.data[pos].icon == 'X':
                pointsX += 1
            if pointsX == 4:
                return 'X'  
            if self.data[pos].icon == 'O':
                pointsO += 1
            if pointsO == 4:
                return 'O'

        #Diagonal2
        pointsX = 0
        pointsO = 0
        for i in self.data:
            sum = 0
            for a in self.data[i].id:
                sum += int(a)
                if sum == self.side-1:
                    if self.data[pos].icon == 'X':
                        pointsX += 1
                    if pointsX == 4:
                        return 'X'  
                    if self.data[pos].icon == 'O':
                        pointsO += 1
                    if pointsO == 4:
                        return 'O'



player1 = Player()

player1.setName(1)
player1.select()

player2 = Player()
player2.setName(2)
if player1.icon == 'X':   
    player2.icon = 'O'
else: player2.icon = 'X'

table = Table()
table.setSide()
table.generate()
table.showId()

while True: 
    table.setSquare(player1)
    table.showId()
    win = table.winner()
    table.setSquare(player2)
    table.showId()
    win = table.winner()
    if win == 'X':
        print('Gana X')
    if win == 'O':
        print('Gana O')