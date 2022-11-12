#Autor do trabalho: Silas Rafael Barreto Prado

'''
Problema escolhido 
- Carteiro: Consiste em encontrar a menor distância total para um entregador passar por todos os endereços 
de entrega ao menos uma vez. Esta solução pode ser aplicada em muitas áreas da logística, como na rota de carteiros 
ou em sistemas de coleta de lixo. 
Foi utilizado para a solução deste problema o algoritmo da Árvore Geradora Mínima.

Funcionamento:
- Passando as informações corretas para o arquivo de entrada no diretório(files/input.txt) o sistema 
inicia uma análise e calcula a menor distancia possível para percorrer, partindo de um ponto inicial, passando por 
todos os pontos(arestas) informados. Por fim ele gera um arquivo de saída no diretório(files/output.txt)
com a conexão entre um ponto e outro e a distância mínima total encontrada.

Padrão do arquivo de entrada:
Os dados do arquivo deverão ser na forma de um grafo não direcionado, onde os valores passados serão a conexão 
de um ponto a outro e seu custo, sendo lidos da seguinte forma:
A primeira linha será o número de vértices(x) e arestas(y).
As demais linhas serão os valores do ponto 1(p1), do ponto 2(p2) e a distância percorrida(distance).

Padrão do arquivo de saída:
O arquivo de saída é gerado assim que o projeto é executado, passando todas as conexões de um ponto ao outro 
em uma lista, e a distância mínima total encontrada. Ao executar o projeto novamente, ele apenas 
sobrescreverá o arquivo de saída.

Alguns exemplos de entrada: 

7 12
0 1 7 
1 3 1
3 2 3
2 4 2 
4 6 2
6 5 8
5 5 3
5 4 4
5 1 1
1 6 8
4 1 3

------

9 14
0 1 1
1 7 11
7 2 8
2 3 3
3 8 7
8 5 4
5 4 2
4 4 1
4 5 2
5 5 9    
5 6 2
6 7 1
6 8 6
8 9 1

------

5 9
1 4 5 
4 0 4
0 3 4
3 2 1 
2 2 5
2 3 3

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
output = gera o resultado no arquivo output.txt

'''


import readInput
import heapq
'utf-8'


def main():
    #variável utilizada para verificar se o arquivo está ou não vazio através da função empty()
    readingFile = readInput.empty('../files/input.txt')

    #abre e lê o arquivo de entrada, e gera o arquivo de saída, se o arquivo não for vazio
    if readingFile == False:

        #executa a função openFile() para abrir o arquivo
        x,y,heap,values = readInput.openFile()

        #executa a função readFile() para ler o arquivo
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
        output.write('Lista com a ligação de um ponto a outro para percorrer a menor distância possível: ')  
        output.write("\n")
        output.write(str(tree))  
        output.write("\n")
        output.write("\n")
        output.write('Distância total mínima encontrada: ' + str(result) + 'Km')  
        output.close()
    #se a entrada estiver vazia, gera o arquivo de saída com a frase 'O arquivo de saída está vazio'
    else:
        output = readInput.output()
        output = (output)  
        output.write('O arquivo de saída está vazio')  
        output.close()

if (__name__ == "__main__"):
    main()











