# Programa que comprueba si un sudoku introducido por el usuario
# es correcto o no.
#
# Para ello deberá cumplir los siguientes requisitos:
#
# a) La Matriz dada es cuadrada
# b) La Matriz debe contener números Válidos:
#   · Los números han de ser enteros
#   · Tiene que haber tantos números como longuitud tenga la columna
#   · El número no puede ser más grande que la longuitud del sudoku
# d) No se pueden repetir números en cada fila
# e) No se pueden repetir números en cada columna

def esValido(sudoku):
    
    if esCuadrado(sudoku) and checkNumerosValidos(sudoku) and checkFilas(sudoku) and checkColumnas(sudoku):
        return True
    else:
        return False

def esCuadrado(sudoku):
    
    numeroFilas = len(sudoku)   
    for fila in sudoku:
        if len(fila) != numeroFilas:
            return False
    return True

def checkNumerosValidos(sudoku):
    return True

def checkFilas(sudoku):
    return True

def checkColumnas(sudoku):
    return True

# Caso Test 1:
sudoku = [[1,2,3],[2,1,3],[3,2,1]]
print (esValido(sudoku))
# >>> True

# Caso Test 2:
sudoku = [[1, 2, 3],[2,1], [3,2,1]]
print (esValido(sudoku))
# >>> False

# Caso Test 3:
sudoku = [[1, 2, 3], [2,1,3],[3,2]]
print (esValido(sudoku))
# >>> False


'''
# Casos test pasados
correcto1 = [[1, 2, 3],
             [2, 3, 1],
             [3, 1, 2]]
print(esValido(correcto1))
correcto2 = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]
print(esValido(correcto2))

incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 3],
               [4, 4, 4, 4]]
print(esValido(incorrecto2))

incorrecto3 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 3, 4],]
print(esValido(incorrecto3))
'''