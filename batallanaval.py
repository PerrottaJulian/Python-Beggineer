tablero = []
for i in range (10):
    linea = []
    for i in range (10):
        linea.append(0)
    tablero.append(linea)
def colocarBarco(cor1, cor2, tablero):
    ver1 = int(str(cor1)[0])
    hor1 = int(str(cor1)[1])
    ver2 = int(str(cor2)[0])
    hor2 = int(str(cor2)[1])

    if ver1 == ver2:
        pos= "Horizontal"
    elif hor1 == hor2:
        pos= "Vertical"
    else:
        pos= "Mal"
    
    if pos == "Vertical":
        for i in range(min(ver1, ver2), max(ver1, ver2)+1):
            tablero[i][hor1] = 2
    elif pos == "Horizontal":
        for i in range(min(hor1, hor2), max(hor1, hor2)+1):
            tablero[ver1][i] = 2
    else:
        print(f"Error: coordenadas {cor1}/{cor2} son incorrectas")
    return tablero
    
def print_tablero(tablero):
    for linea in tablero:
        print(linea)


tablero = colocarBarco(32, 82, tablero)
tablero = colocarBarco(45, 78, tablero)
tablero = colocarBarco(11, 13, tablero)

print_tablero(tablero)