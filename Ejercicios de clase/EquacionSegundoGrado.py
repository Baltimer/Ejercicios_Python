# Programa que resuelve una equación de segundo grado
#
# Autores: Luis Cifre, Guillem Cirer

# Funcion que resuelve la ecuación


def resolverEquacionSegundoGrado (a, b, c):
    
    import math

    interiorRaiz = b**2 -(4*a*c)
    if interiorRaiz >= 0:
        resultadoRaiz = math.sqrt(interiorRaiz)
        x1 = (-b + resultadoRaiz) / 2*a
        x2 = (-b - resultadoRaiz) / 2*a
        return x1, x2
    else:
        return NONE

# Comprobar si resuelve la ecución correctamente

# Caso Test 1
a = 1
b = -7
c = 10
# >>> x1 = 5
# >>> x2 = 2
x1, x2 = resolverEquacionSegundoGrado(a, b, c)

if x1 == 5 and x2 == 2:
    print ("Test OK")
else:
    print ("Test FAIL")