
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

    print()

    grafo = criar_grafo()
    inserir_vertice(grafo[0],grafo[1], "A")
    inserir_vertice(grafo[0],grafo[1], "B")
    inserir_vertice(grafo[0],grafo[1], "C")
    inserir_vertice(grafo[0],grafo[1], "D")
    inserir_vertice(grafo[0],grafo[1], "E")

    

    exibir_grafo(grafo[0],grafo[1])


    inserir_aresta(grafo[0],grafo[1],"A","B")
    

    print(vizinhos(grafo[0],grafo[1],"A"))
    listar_vizinhos(grafo[0],grafo[1],"A")

    exibir_grafo(grafo[0],grafo[1])

    caminho = ["A","B","C","D","E"]

    print(percurso_valido(grafo[0],grafo[1],caminho))

    graus = grau_vertices(grafo[0],grafo[1])

    for chave, valor in graus.items():
        print(f"Chave: {chave} | Valor: {valor}")

    print()
    return


if __name__ == "__main__":
    main()
