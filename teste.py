import sys
import time
import math

from fermat import primo_fermat
from pascal import primo_pascal
from rsa import gerando_chaves_rsa
from rsa import encontrar_modulo_inverso
from rsa import criptografar
from rsa import decriptografar


def leitor_numero(quantidade_digitos):
    nome_arquivo = str(quantidade_digitos) + '_digitos.txt'
    with open(nome_arquivo) as arquivo:
        for numero in arquivo:
            yield int(numero)
    

def teste_pascal(numero):
    resultado  =False
    tempo_total=0.0

    tempo_inicio = time.perf_counter()
    resultado = primo_pascal(numero)
    tempo_fim = time.perf_counter()
    tempo_total = tempo_fim - tempo_inicio

    return resultado, tempo_total

def teste_fermat(numero):
    resultado  =False
    tempo_total=0.0

    tempo_inicio = time.perf_counter()
    resultado = primo_fermat(numero)
    tempo_fim = time.perf_counter()
    tempo_total = tempo_fim - tempo_inicio

    return resultado, tempo_total

def teste_pascal_fermat():
    tempo_total_teste_pascal = 0.0
    tempo_total_teste_fermat = 0.0

    tempo_unitario_fermat = 0.0
    tempo_unitario_pascal = 0.0

    resultado_fermat = False
    resultado_pascal = False
    
    quantidade_erros = 0
    
    numero_digitos = int(sys.argv[1])

    quantidade_testes = 0

    for numero in leitor_numero(numero_digitos):
        # PASCAL
        resultado_pascal, tempo_unitario_pascal = teste_pascal(numero)
        tempo_total_teste_pascal += tempo_unitario_pascal

        # FERMAT
        resultado_fermat, tempo_unitario_fermat = teste_fermat(numero)
        tempo_total_teste_fermat += tempo_unitario_fermat

        if ( resultado_fermat != resultado_pascal ):
            quantidade_erros +=1

        quantidade_testes +=1
        print()
        print('>> Teste : ', quantidade_testes)
        print('>> Numero: ', numero)        
        print('> PASCAL')
        print('>> Result: ', resultado_pascal)
        print('> FERMAT')
        print('>> Result: ', resultado_fermat)
        print()
    
    tempo_medio_pascal = tempo_total_teste_pascal / quantidade_testes
    tempo_medio_fermat = tempo_total_teste_fermat / quantidade_testes
    taxa_media_erros_fermat = quantidade_erros / quantidade_testes

    print('> PASCAL')
    print('>> Tempo total      : ', tempo_total_teste_pascal)
    print('>> Quantidade testes: ', quantidade_testes)
    print('>> Tempo medio      : ', tempo_medio_pascal)

    print()

    print('> FERMAT')
    print('>> Tempo total      : ', tempo_total_teste_fermat)
    print('>> Quantidade testes: ', quantidade_testes)
    print('>> Tempo medio      : ', tempo_medio_fermat)
    print('>> Taxa media erros : ', taxa_media_erros_fermat)

def teste_forca_bruta_rsa(mensagem_criptografada, chave_publica):
    n = chave_publica[0]
    e = chave_publica[1]
    p = int(math.ceil(math.sqrt(n)))
    if ( p % 2 == 0):
        p = p - 1
    while(True):
        if ( n % p == 0):
            break
        p -= 2
    q = n // p
    d = encontrar_modulo_inverso(e, (p-1)*(q-1))
    return d


def teste_rsa(tamanho_chave=512):
    (chave_publica, chave_privada) = gerando_chaves_rsa(tamanho_chave=tamanho_chave)
    mensagem = int(input('Entre com um numero: '))
    print('Chave publica (n,e)     : ', chave_publica)

    mensagem_criptografada = criptografar(mensagem, chave_publica)
    print('Mensagem criptografada  : ', mensagem_criptografada)
    # mensagem_decriptografada = decriptografar(mensagem_criptografada, chave_privada)
    # print('Mensagem decriptografada: ', mensagem_decriptografada)

    print('Encontrando chave privada pela forca bruta...')
    d = teste_forca_bruta_rsa(mensagem, chave_publica)
    chave_privada = (chave_publica[0], d)
    mensagem_decriptografada = decriptografar(mensagem_criptografada, chave_privada)
    print('Mensagem decriptografada: ', mensagem_decriptografada)
    

    

