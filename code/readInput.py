import heapq
import random
import os

#função para abrir o arquivo de entrada com o método open()
def openFile():
    heap = []
    with open('generated-files/input.txt', encoding='utf-8') as fp:  
        for i, line in enumerate(fp):
            if i == 0:
                vert1, vert2 = line.split()
                vert1 = int(vert1)
                vert2 = int(vert2)

            break

    values = [[] * vert1 for i in range(vert1)]
    return vert1, vert2, heap, values

#função para ler todas as linhas do arquivo de entrada 
def readFile():
    x, y, heap, values = openFile()

    for j in range(y):
        with open('generated-files/input.txt') as fp:  
            for i, line in enumerate(fp):
                if i >= 1 and i <= j:  
                    p1, p2, distance = line.split()
                    p1 = int(p1)  
                    p2 = int(p2) 
                    distance = int(distance) 
                    values[p1].append((p2, distance))
                    values[p2].append((p1, distance))
                    init = random.randint(0, x - 1)

    return p1, p2, distance, values, init

#função para gerar o arquivo de saída
def output():

    output = open('generated-files/output.txt', 'w', encoding='utf-8')  

    return output

#função para verificar se o arquivo está vazio
def empty(path):
    return os.stat(path).st_size==0



