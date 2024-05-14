side = int(input('lado: '))

for r in range(1,side+1):
    rows = []
    cols = []
    for c in range(1,side+1):
        row = str(r)
        col = str(c)
        
        square = ''
        square += str(r)
        square += str(c)
        square = f'_{square}_'
        #square = f'___'
        cols.append(square)

    rows.append(cols)
    rowStr = str(rows)
    print (rowStr.replace('[', '').replace(']', '').replace(',', '|').replace("'", '').replace(' ', ''))

