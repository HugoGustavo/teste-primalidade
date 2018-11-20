import sys
import time

from fermat import primo_fermat
from pascal import primo_pascal

def gerador_numeros(i, j):
    inicio = 2 ** i
    fim = 2 ** j
    i = inicio
    while ( i < fim ):
        yield i
        i+=1

def teste_pascal(numero, resultado, tempo_total=0.0):
    tempo_inicio = time.perf_counter()
    resultado = primo_pascal(numero)
    tempo_fim = time.perf_counter()
    tempo_total = tempo_fim - tempo_inicio

def teste_fermat(numero, resultado, tempo_total=0.0, confianca=0.05):
    tempo_inicio = time.perf_counter()
    resultado = primo_fermat(numero, confianca=confianca)
    tempo_fim = time.perf_counter()
    tempo_total = tempo_fim - tempo_inicio

def teste_pascal_fermat():
    tempo_total_teste_pascal = 0.0
    tempo_total_teste_fermat = 0.0

    tempo_unitario_fermat = 0.0
    tempo_unitario_pascal = 0.0

    resultado_fermat = False
    resultado_pascal = False
    
    quantidade_erros = 0

    i = int(sys.argv[1])
    j = int(sys.argv[2])
    confianca = float(sys.argv[3])

    quantidade_testes = 0

    for numero in gerador_numeros(i,j):
        # PASCAL
        teste_pascal(numero, resultado_pascal, tempo_unitario_pascal)
        tempo_total_teste_pascal += tempo_unitario_pascal

        # FERMAT
        teste_fermat(numero, resultado_fermat, tempo_unitario_fermat, confianca=confianca)
        tempo_total_teste_fermat += tempo_unitario_fermat

        if ( resultado_fermat != resultado_pascal ):
            quantidade_erros +=1

        quantidade_testes +=1
        
    
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