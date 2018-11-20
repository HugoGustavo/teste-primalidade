import sys

def get_linha_pascal(indice):
    atual = 1
    for i in range(indice >> 1):
        x = atual * ( indice-i )//( i + 1 )
        yield x
        atual = x

def primo_pascal(numero):
    if ( numero < 2 ):
        return False
    for numero_pascal in get_linha_pascal(numero):
        if ( numero_pascal != 1 and numero_pascal % numero != 0):
            return False
    return True