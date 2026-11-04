
def criar_grafo():

    matriz = [[]]
    vertices = []

    return (matriz,vertices)


def inserir_vertice(matriz: list[list], vertices: list, vertice: str):

    if vertice in vertices:
        return

    vertices.append(vertice)

    for linha in matriz:
        linha.append(0)

    qtdVertices = len(matriz[0])

    novaLinha = []
    
    for vtx in range(qtdVertices):
        novaLinha.append(0)

    matriz.append(novaLinha)

    return


def inserir_aresta(matriz: list[list], vertices: list, origem: str, destino: str, nao_direcionado=False):

    if origem not in vertices or destino not in vertices:
        inserir_vertice(matriz,vertices,origem)
        inserir_vertice(matriz,vertices,destino)

    idxI = vertices.index(origem)
    idxJ = vertices.index(destino)

    matriz[idxI][idxJ] = 1

    if nao_direcionado:
        matriz[idxJ][idxI] = 1

    return


def remover_vertice(matriz: list[list], vertices: list, vertice: str):

    if vertice not in vertices:
        return

    idxV = vertices.index(vertice)

    matriz.pop(idxV)

    for linha in matriz:
        linha.pop(idxV)

    vertices.pop(idxV)        

    return

def remover_aresta(matriz: list[list], vertices: list, origem: str, destino: str, nao_direcionado=False):
    
    if origem not in vertices or destino not in vertices:
        return

    idxI = vertices.index(origem)
    idxJ = vertices.index(destino)

    if matriz[idxI][idxJ] == 0 and not nao_direcionado:
        raise Exception("Remoção de arestas não existentes ou Grafo não direcionado")

    matriz[idxI][idxJ] = 0

    if nao_direcionado:
        matriz[idxJ][idxI] = 0
    
    return


def existe_aresta(matriz, vertices, origem, destino):

    if origem not in vertices or destino not in vertices:
        return

    idxI = vertices.index(origem)
    idxJ = vertices.index(destino)

    if matriz[idxI][idxJ] == 1:
        return True
    
    return False


def vizinhos(matriz: list[list], vertices: list, vertice: str):

    if vertice not in vertices:
            return

    idxV = vertices.index(vertice)

    listaVizinhos = []

    for contador, vtx in enumerate(matriz[idxV]):
        if vtx == 1:
            listaVizinhos.append(vertices[contador])
        
    return listaVizinhos


def grau_vertices(matriz: list[list], vertices: list, nao_direcionado=False):

    graus = {}  

    for vtx in vertices:

        if not nao_direcionado: 

            idxV = vertices.index(vtx)

            linha = matriz[idxV]

            gSaida = sum(linha)
            gEntrada = 0
            gTotal = 0

            for coluna in range(len(matriz)):
                gEntrada += matriz[coluna][idxV]

            gTotal = gSaida + gEntrada
            graus[vtx] = {"saida": gSaida, "entrada": gEntrada, "total": gTotal}

        else:

            idxV = vertices.index(vtx)
            
            linha = matriz[idxV]
            
            gSaida = sum(linha)

            graus[vtx] = gSaida

    return graus


def percurso_valido(matriz: list[list], vertices: list, caminho: list):

    for contador in range(len(caminho)-1):


        if not existe_aresta(matriz, vertices, caminho[contador], caminho[contador + 1]):
            return False


    return True


def listar_vizinhos(matriz: list[list], vertices: list, vertice: str):

    if vertice not in vertices:
        return

    listaVizinhos = vizinhos(matriz,vertices,vertice)

    print(f"Vizinhos de {vertice}: " + "{"+ ", ".join(listaVizinhos) + "}")


def exibir_grafo(matriz, vertices):

    print("   " + "  ".join(vertices))

    for i in range(len(matriz)-1):
        print(vertices[i] + "  " + "  ".join(map(str,matriz[i])))
    


def main():

    grafo = None
    nao_direcionado = None

    while (True):

        print(f"""
Escolha uma das opções abaixo:
1. Criar grafo
2. Inserir vértice
3. Inserir aresta
4. Remover vértice
5. Remover aresta
6. Verificar se aresta existe
7. Listar vizinhos
8. Exibir grau dos vértices
9. Verificar se percurso é válido
10. Exibir grafo
0. Encerrar
            """)

        option = input("-> ")

        if option != "0" and option != "1" and grafo is None:
            print("Necessário criar um grafo")
            continue

        match option:
            case "1":
                nao_direcionado = False if input("O grafo é direcionado? (Sim ou Não): ").upper() == "SIM" else True
                print(nao_direcionado)
                if grafo:
                    print("Grafo reiniciado")
                else:
                    print("Grafo criado")
                grafo = criar_grafo()
            case "2":
                v = input("Digite um caracter para representar o vértice: ").upper()
                print(nao_direcionado)
                if len(v) == 1:
                    inserir_vertice(grafo[0], grafo[1], v)
                else:
                    print("Não é aceito mais de um caracter")
            case "3":
                v1 = input("Digite o vértice 1: ").upper()
                v2 = input("Digite o vértice 2: ").upper()
                if len(v1) == 1 and len(v2) == 1:
                    inserir_aresta(grafo[0], grafo[1], v1, v2, nao_direcionado)
                    print("Aresta criada")
                else:
                    print("Não é aceito mais de um caracter por vértice")
            case "4":
                v = input("Escolha o vértice: ").upper()
                if v in grafo[1]:
                    remover_vertice(grafo[0], grafo[1], v)
                else:
                    print("Vértice não existe")
            case "5":
                v1 = input("Digite o vértice 1: ").upper()
                v2 = input("Digite o vértice 2: ").upper()
                if v1 in grafo[1] and v2 in grafo[1]:
                    remover_aresta(grafo[0], grafo[1], v1, v2, nao_direcionado)
                else:
                    print("Digite vértices válidos")
            case "6":
                v1 = input("Digite o vértice 1: ").upper()
                v2 = input("Digite o vértice 2: ").upper()
                if existe_aresta(grafo[0], grafo[1], v1, v2):
                    print("Existe")
                else:
                    print("Não existe")
            case "7":
                v = input("Escolha o vértice: ").upper()
                listar_vizinhos(grafo[0], grafo[1], v)
            case "8":
                graus = grau_vertices(grafo[0], grafo[1], nao_direcionado)

                print("Vértice | Saída | Entrada | Total")
                for idx, values in graus.items():
                    print(f"   {idx}    |   {values["saida"]}   |    {values["entrada"]}    |   {values["total"]}")
            case "9":
                l = input(f"Vértices existentes: {" ".join(grafo[1])}\nDigite os vértices em apenas uma linha separados por espaço: ").upper()
                print(l.split(" "))
                if percurso_valido(grafo[0], grafo[1], l.split(" ")):
                    print("É válido")
                else:
                    print("Não é válido")
            case "10":
                if grafo[0][0]:
                    exibir_grafo(grafo[0], grafo[1])
                else:
                    print("Grafo vazio")
            case "0":
                break
            case _:
                print("Opção inválida")
    return
    # print()

    # grafo = criar_grafo()
    # inserir_vertice(grafo[0],grafo[1], "A")
    # inserir_vertice(grafo[0],grafo[1], "B")
    # inserir_vertice(grafo[0],grafo[1], "C")
    # inserir_vertice(grafo[0],grafo[1], "D")
    # inserir_vertice(grafo[0],grafo[1], "E")

    

    # exibir_grafo(grafo[0],grafo[1])


    # inserir_aresta(grafo[0],grafo[1],"A","B")
    

    # print(vizinhos(grafo[0],grafo[1],"A"))
    # listar_vizinhos(grafo[0],grafo[1],"A")

    # exibir_grafo(grafo[0],grafo[1])

    # caminho = ["A","B","C","D","E"]

    # print(percurso_valido(grafo[0],grafo[1],caminho))

    # graus = grau_vertices(grafo[0],grafo[1])

    # for chave, valor in graus.items():
    #     print(f"Chave: {chave} | Valor: {valor}")

    # print()


if __name__ == "__main__":
    main()
