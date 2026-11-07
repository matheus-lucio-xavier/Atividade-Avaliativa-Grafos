def criar_grafo():
    vertices = []
    arestas = []

    return vertices, arestas


def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)

    return

def inserir_aresta(vertices, arestas, origem, destino, direcionado=True):
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
            inserir_vertice(vertices, destino)

    arestas.append([origem, destino])

    if not direcionado:
        arestas.append([destino, origem])

    return

def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        vertices.pop(vertices.index(vertice))

        for origem, destino in arestas:
            if origem == vertice or destino == vertice:
                arestas.pop(arestas.index([origem, destino]))

    return

def remover_aresta(arestas, origem, destino, direcionado=True):
    for _origem, _destino in arestas:
        if _origem == origem and _destino == destino:
            arestas.pop(arestas.index([_origem, _destino]))

        if _origem == destino and _destino == origem and not direcionado:
            arestas.pop(arestas.index([_destino, _origem]))

    return

def existe_aresta(arestas, origem, destino):
    for _origem, _destino in arestas:
        if _origem == origem and _destino == destino:
            return True

    return False


def vizinhos(vertices, arestas, vertice):
    vizinhos = []
    
    for _origem, _destino in arestas:
        if _origem == vertice:
            vizinhos.append(_destino)

    return vizinhos


def grau_vertices(vertices, arestas, direcionado = True):
    graus = {}

    for _vertice in vertices:
        gEntrada = 0
        gSaida = 0
        gTotal = 0

        if not direcionado:
            for _origem, _destino in arestas:
                if _origem == _vertice or _destino == _vertice:
                    gSaida += 1
        else:
            for _origem, _destino in arestas:
                if _origem == _vertice:
                    gSaida += 1
                if _destino == _vertice:
                    gEntrada += 1

        gTotal = gEntrada + gSaida
                            
        graus[_vertice] = {"entrada": gEntrada, "saida": gSaida, "total": gTotal}

    return graus

def percurso_valido(arestas, caminho):
    for i in range(len(caminho)-1):
        if not existe_aresta(arestas, caminho[i], caminho[i+1]):
            return False

    return True


def listar_vizinhos(vertices, arestas, vertice):
    if vertice not in vertices:
            return
    
    listaVizinhos = vizinhos(vertices, arestas, vertice)
    
    print(f"Vizinhos de {vertice}: " + "{"+ ", ".join(listaVizinhos) + "}")


def exibir_grafo(vertices, arestas):
    print("   " + "  ".join(vertices)+"\n")

    for _origem, _destino in arestas:
        print("   "+_origem+"->"+_destino+"   ")

    """
    Exibe todas as arestas do grafo.

    Passos:
    1. Exibir a lista de vértices.
    2. Exibir todas as arestas no formato (origem -> destino).
    """
    pass


def main():
    
    vertices = None
    arestas = None
    direcionado = None

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

        if option != "0" and option != "1" and vertices is None and arestas is None:
            print("Necessário criar um grafo")
            continue

        match option:
            case "1":
                direcionado = True if input("O grafo é direcionado? (s/n): ").upper() == "S" else False
                if vertices and arestas:
                    print("Grafo reiniciado")
                else:
                    print("Grafo criado")
                vertices, arestas = criar_grafo()
                input()
            case "2":
                v = input("Digite um caracter para representar o vértice: ").upper()
                if len(v) > 0:
                    inserir_vertice(vertices, v)
                else:
                    print("É necessario pelo menos um caracter")
                input()
            case "3":
                v1 = input("Digite o vértice 1: ").upper()
                v2 = input("Digite o vértice 2: ").upper()
                if len(v1) > 0 and len(v2) > 0:
                    inserir_aresta(vertices, arestas, v1, v2, direcionado)
                    print("Aresta criada")
                else:
                    print("É necessario pelo menos um caracter por vertice")
                input()
            case "4":
                v = input("Escolha o vértice: ").upper()
                if v in vertices:
                    remover_vertice(vertices, arestas, v)
                else:
                    print("Vértice não existe")
                input()
            case "5":
                v1 = input("Digite o vértice 1: ").upper()
                v2 = input("Digite o vértice 2: ").upper()
                if v1 in vertices and v2 in vertices:
                    remover_aresta(arestas, v1, v2, direcionado)
                else:
                    print("Digite vértices válidos")
                input()
            case "6":
                v1 = input("Digite o vértice 1: ").upper()
                v2 = input("Digite o vértice 2: ").upper()
                if existe_aresta(arestas, v1, v2):
                    print("Existe")
                else:
                    print("Não existe")
                input()
            case "7":
                v = input("Escolha o vértice: ").upper()
                listar_vizinhos(vertices, arestas, v)
                input()
            case "8":
                graus = grau_vertices(vertices, arestas, direcionado)

                print("Vértice | Entrada | Saída | Total")
                for idx, values in graus.items():
                    print(f"  {idx}    |    {values["entrada"]}    |   {values["saida"]}   |   {values["total"]}")
                input()
            case "9":
                l = input(f"Vértices existentes: {" ".join(vertices)}\nDigite os vértices em apenas uma linha separados por espaço: ").upper()
                print(l.split(" "))
                if percurso_valido(arestas, l.split(" ")):
                    print("É válido")
                else:
                    print("Não é válido")
                input()
            case "10":
                if vertices or arestas:
                    exibir_grafo(vertices, arestas)
                else:
                    print("Grafo vazio")
                input()
            case "0":
                break
            case _:
                print("Opção inválida")
    return


if __name__ == "__main__":
    main()
