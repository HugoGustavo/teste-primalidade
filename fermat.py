import sys
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

def primo_fermat(n, confianca=0.05):
    numeros_testados = set()
    porcentagem_numeros_testados = 0.0
    y = 0
    while ( porcentagem_numeros_testados < (1-confianca) and y != 1):
        a = randint(1, n-1)
        if a not in numeros_testados:
            numeros_testados.add(a)
            y = calcular_fermat(a, n)
            if ( y != 1 ):
                return False
            porcentagem_numeros_testados = len(numeros_testados) / n
    return True

