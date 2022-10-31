#Autor do trabalho: Silas Rafael Barreto Prado

'''
Problema escolhido 
- Carteiro: Consiste em encontrar um trajeto fechado de distância mínima que percorre
todas arestas de um grafo ao menos uma vez. Esta solução pode ser aplicada em muitas áreas da logística,
como na rota de carteiros. Foi utilizado para a solução deste problema os algoritmos de Dijkstra e Arvore Geradora Mínima.

Funcionamento:
- Passando as informações corretas para o arquivo de entrada(inputFile.txt) o sistema inicia uma análise e 
calcula a menor distancia possível para percorrer, partindo de um ponto inicial, 
e passando por todos os pontos(arestas) informados. Quando o algoritmo recebe as informações do grafo, 
a partir do ponto inicial, ele analisa a menor distância para conectar todas as vértices através 
dos valores das arestas passadas no arquivo de entrada. Por fim ele gera um arquivo de saída 
com a conexão entre os pontos e a distância mínima encontrada.

Variáveis principais:
x = número vértices
y = número arestas
points = lista de arestas
init = ponto inicial
p1 = primeiro ponto de conexão
p2 = segundo ponto de conexão
points = 
distance = distância percorrida
result = distância total mínima encontrada
tree = lista com as conexões que gerarão um menor custo
output = gera o resultado no arquivo outputFile.txt

Padrão do arquivo de entrada:
Os dados do arquivo deverão ser na forma de um grafo conectado, valorado e não direcionado, onde esses dados
serão a conexão de um ponto a outro e seu custo, sendo lidos da seguinte forma:
A primeira linha será o número de vértices(x) e arestas(y).
As demais linhas serão os valores do ponto 1(p1), do ponto 2(p2) e a distância percorrida(distance).

Alguns exemplos de entrada: 

7 12
3 1 2 
3 5 7
5 3 4
2 3 5 
3 4 7
2 5 8
2 6 3
3 3 4
4 5 2
0 3 8
5 5 3

------

9 14
0 1 11
3 7 5
1 2 8
3 7 3
2 3 7
3 5 4
3 8 2
5 4 13
3 5 14
4 5 9    
5 6 2
3 7 1
6 8 6
7 9 10

------

7 15
0 1 0 
0 4 4
2 3 4
1 1 1 
0 2 5
2 3 3
1 6 3
3 3 4
2 5 2
4 5 3
5 5 1

O arquivo de saída é gerado assim que o projeto é executado, e nas próximas vezes que o
projeto for executado, apenas sobrescreverá o arquivo de saída.

'''


import readInput
import heapq
'utf-8'


def main():
    readingFile = readInput.empty('input.txt')


    if readingFile == False:

        x,y,heap,values = readInput.openFile()

        p1, p2, distance, values, init= readInput.readFile()

        for (p, distance) in values[init]:
            heapq.heappush(heap, (distance, init, p))

        points = 0  
        result = 0  
        marked = [init]  
        tree = []  

        while points < x - 1:
            while True:
                (distance, p1, p2) = heapq.heappop(heap)
                if p2 not in marked:
                    break
            marked.append(p2)

            result += distance
            tree.append((p1, p2))
            points += 1

            for (p, distance) in values[p2]:
                if p not in marked:
                    heapq.heappush(heap, (distance, p2, p))



        output = readInput.output()
        output =(output)  
        output.write('Ordem dos pontos de entrega para percorrer a menor distância possível: ')  
        output.write("\n")
        output.write(str(tree))  
        output.write("\n")
        output.write("\n")
        output.write('Distância total: ' + str(result) + 'Km')  
        output.close()
    else:
        output = readInput.output()
        output = (output)  
        output.write('O arquivo de saída está vazio')  
        output.close()

if (__name__ == "__main__"):
    main()











