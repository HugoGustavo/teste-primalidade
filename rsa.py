import random
from fermat import primo_fermat
from fermat import exponenciacao_modular

def maximo_divisor_comun(a, b):
    while( a != 0 ):
        (a,b) = (b%a, a)
    return b

def encontrar_modulo_inverso(a, m):
    if ( maximo_divisor_comun(a, m) != 1):
        return None
    
    (u1, u2, u3) = (1, 0, a)
    (v1, v2, v3) = (0, 1, m)

    while( v3 != 0 ):
        q = u3 // v3
        (v1, v2, v3, u1, u2, u3) = (u1-q*v1, u2-q*v2, u3-q*v3, v1, v2, v3)
    return u1 % m

def gerando_numero_primo_grande(tamanho_chave=512):
    while(True):
        numero = random.randrange(2**(tamanho_chave-1), 2**tamanho_chave)
        if ( primo_fermat(numero) ):
            return numero

def gerando_chaves_rsa(tamanho_chave=512):
    # Gerando P
    p = gerando_numero_primo_grande(tamanho_chave=tamanho_chave)
    # Gerando Q
    q = gerando_numero_primo_grande(tamanho_chave=tamanho_chave)
    # Gerando N = P * Q
    n = p * q

    # Gerando E que é primo relativo de (P-1)*(Q-1)
    while( True ):
        e = random.randrange( 2 ** (tamanho_chave-1), 2 ** tamanho_chave)
        if ( maximo_divisor_comun(e, (p-1)*(q-1)) == 1):
            break
    
    # Calculando d que eh modulo inverso de e
    d = encontrar_modulo_inverso(e, (p-1)*(q-1))
    chave_publica = (n, e)
    chave_privada = (n, d)

    return (chave_publica, chave_privada)

def criptografar(mensagem, chave_publica):
    return exponenciacao_modular(mensagem, chave_publica[1], chave_publica[0])

def decriptografar(mensagem, chave_privada):
    return exponenciacao_modular(mensagem, chave_privada[1], chave_privada[0])