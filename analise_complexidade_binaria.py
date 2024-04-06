import random as rd
import time
import matplotlib.pyplot as plt 
import numpy as np

''' quick-sort'''

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)
        
def partition(arr, left, right):
    i = left
    j = right -1
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        
        while j > left and arr[j] >= pivot:
            j -= 1
            
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i


''' busca binária com análise de complexidade'''


def buscabinaria(lista,chave):
    pos_inic = 0
    pos_final = len(lista) - 1
    iteracao = 4 # 2 acima + break do while + return do final 
    
    while pos_inic <= pos_final:
        pos_mid = (pos_inic + pos_final)//2 # obs // divide nosso número e pega apenas a parte inteira
        iteracao += 1
        if chave == lista[pos_mid]:
            iteracao += 2 # o return + o if q não seria contabilizado 
            return print ('Posição da chave ', chave, 'na lista:', pos_mid + 1, 'e foram realizadas', iteracao + 1, 'iterações')
        if chave < lista[pos_mid]:
            pos_final = pos_mid - 1  # -1 economiza processo
            iteracao += 1
        if chave > lista[pos_mid]:
            pos_inic = pos_mid + 1 # +1 economiza uma casa a ser analizada (economiza processo)
            iteracao += 1
        iteracao += 3 #estamos somando os 3 ifs    
    return print("A chave",chave, "não se encontra na lista", 'e foram realizadas', iteracao, 'iterações')


# vamos criar uma lista com números alearórios de 0 a 100 (sem repetição)
lista100 = []
for i in range (1,101): # criamos uma lista de 100 números
    lista100.append(i)
rd.shuffle(lista100) # embaralha os elementos da nossa lista de 100 números

''' 10 elementos na lista'''

print('LISTA COM 10 ELEMENTOS - PIOR CASO')
lista10 = lista100[0:10]
quicksort(lista10, 0, len(lista10)-1)
print(lista10)

inicio = time.time() # grava o tempo inicial
buscabinaria(lista10, lista10[9])
fim = time.time() # grava o tempo final
tempo_total = fim - inicio # calcula o tempo total decorrido
print(f"Tempo de execução: {tempo_total} segundos")


'''30 elementos na lista'''

print('\nLISTA COM 30 ELEMENTOS - PIOR CASO')
lista30 = lista100[0:30] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista30,0, len(lista30)-1) # colocando-a em ordem
print(lista30)
buscabinaria(lista30, lista30[29])


'''50 elementos na lista'''

print('\nLISTA COM 50 ELEMENTOS - PIOR CASO')
lista50 = lista100[0:50] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista50,0, len(lista50)-1) # colocando-a em ordem
print(lista50)
buscabinaria(lista50, lista50[49])


'''100 elementos na lista'''

print('\nLISTA COM 100 ELEMENTOS - PIOR CASO')
quicksort(lista100,0, len(lista100)-1) # colocando-a em ordem
print(lista100)
inicio = time.time() # grava o tempo inicial
buscabinaria(lista100, lista100[99])
fim = time.time() # grava o tempo final
tempo_total = fim - inicio # calcula o tempo total decorrido
print(f"Tempo de execução: {tempo_total} segundos")


''' plotando o gráfico'''

ypoints = np.array([23,28,33,38])
xpoints = np.array([10,30,50,100])
plt.ylabel('número de iterações')
plt.xlabel("Tamanho da nossa matriz")
plt.title('Análise de complexidade da busca BINÁRIA - pior caso')
plt.plot(xpoints, ypoints, 'o:b') 
plt.show()

