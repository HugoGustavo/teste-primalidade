import sys
import math
from random import randint

def exponenciacao_modular(base, expoente, modulo):
    x = 1
    potencia = base % modulo
    while ( expoente != 0 ):
        if ( expoente & 1 == 1 ):
            x = (x * potencia) % modulo
        potencia = ( potencia ** 2 ) % modulo
        expoente = expoente >> 1
    return x

def calcular_fermat(a, n):
    return exponenciacao_modular(a, n-1, n)

def primo_fermat(n):
    numeros_testados = set()

    # quantidade de numeros a serem testados ( numero de bits do meu numero)
    confianca = int(math.log2(n))
    y = 0
    while ( len(numeros_testados) < confianca and y != 1):
        a = randint(1, n-1)
        if a not in numeros_testados:
            numeros_testados.add(a)
            y = calcular_fermat(a, n)
            if ( y != 1 ):
                return False
            numeros_testados.add(a)
    return True

