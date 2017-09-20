from random import randint#Los valores que se introducen tambien se incluyen en el random.


tamaño = int(input("Elija las dimensiones del tablero (debe ser cuadrado): "))
celulas = int(input("Cuantas células vivas desea? No debe sobrepasar "+str(tamaño*tamaño)+": "))

def crea_filas_columnas(alarm,cantidad):#1
    """
    Entradas: (alarm) funciona unicamente como una alarma y (cantidad). (alarm) = (cantidad).
    Restricciones: (cantidad) se va a ver limitado por un determiado rango.
    Salida: una matriz con (cantidad) filas y columnas.
    Esta función recibe dos parámetros, uno de ellos unicamente sirve para determinar el caso base (alarm),
    y (cantidad) determina la cantidad de filas; al mismo tiempo que es parámetro para (crea_columnas) y determina la cantidad de columnas.
    """
    if  alarm == 0:
        return []

    else:
        resultado = [crea_columnas(cantidad)]
        return resultado + crea_filas_columnas(alarm-1,cantidad)

def crea_columnas(cantidad):#2
    """
    Entrada: Un número(cantidad).
    Restricción: (cantidad) se va a ver limitado en un determinado rango.
    Salida: una lista con (cantidad) elementos.
    La cantidad de elementos en la lista retornada indicarán la cantidad de columnas en el tablero.
    """
    if cantidad == 0:
        return []

    else:
        lista = ["-"]
        resultado = (lista) + (crea_columnas(cantidad-1))
        return resultado 


def introducir_celulas_p(celulas):#1
    """
    """
    tablero = crea_filas_columnas(tamaño,tamaño)
    return introducir_celulas_aux(celulas,tablero)

def introducir_celulas_aux(celulas,mesa):#2
    """
    """
    f_elegida = randint(0,len(mesa)-1)
    c_elegida = randint(0,len(mesa[0])-1)

    if celulas == 0:
        return mesa

    elif celulas != 0:

        if mesa[f_elegida][c_elegida] == "*":
            return introducir_celulas_aux(celulas,mesa)

        else:
            mesa[f_elegida][c_elegida] = "*"
            return introducir_celulas_aux(celulas-1,mesa)


def imprimir(matriz,posicion,tamaño):#1
    if posicion != tamaño:
        imprimir_columnas(matriz[posicion],0,tamaño)
        imprimir(matriz,posicion+1,tamaño)

def imprimir_columnas(fila,posicion,tamaño):#2
    if tamaño != posicion:
        print (fila[posicion],end="  ")
        imprimir_columnas(fila,posicion+1,tamaño)
    else:
        print ("\n")

generacion = introducir_celulas_p(celulas)
imprimir(generacion,0,tamaño)

    


    


#print (crea_filas_columnas(tamaño,tamaño))

