lista_grafo = {}

def add_vertice(vertice):
    if vertice in lista_grafo:
        print("Vertice ja existe no grafo")
    else:
        lista_grafo[vertice] = []

def add_aresta(vertice1, vertice2):
    if vertice1 in lista_grafo and vertice2 in lista_grafo:
        lista_grafo[vertice1].append(vertice2)
        lista_grafo[vertice2].append(vertice1)
    else:
        print("Ambos os vertices precisam estar registrados no grafo")

def add_aresta_direcionada(vertice1, vertice2):
    if vertice1 in lista_grafo and vertice2 in lista_grafo:
        lista_grafo[vertice1].append(vertice2)
    else:
        print("Ambos os vertices precisam estar registrados no grafo")

def remove_vertice(vertice):
    for aux in lista_grafo:
        if vertice in lista_grafo[aux]:
            lista_grafo[aux].remove(vertice)
    lista_grafo.pop(vertice)

def remove_aresta(vertice1, vertice2):
    lista_grafo[vertice1].remove(vertice2)
    lista_grafo[vertice2].remove(vertice1)

def checar_percurso(vertice1, vertice2, checked = []):
    if vertice2 in lista_grafo[vertice1]:
        return True
    elif vertice1 not in checked:
        for aux in lista_grafo[vertice1]:
            return checar_percurso(aux, vertice2)
        checked.append(vertice1)
    else:
        return False

running = True

while running:
    print("==================================================")
    print("Escolha uma opcao:")
    print("1 >> Ler grafo")
    print("2 >> Criar vertice")
    print("3 >> Criar aresta")
    print("4 >> Remover vertice")
    print("5 >> Remover aresta")
    print("6 >> Calcular o grau de um vertice")
    print("7 >> Checar pela adjacencia entre vertices")
    print("8 >> Listar os vizinhos de um vertice")
    print("9 >> Verificar por um percurso")
    print("0 >> Encerrar")

    option = int(input("Digite: "))

    match option:
        case 0:
            running = False
        case 1:
            print(lista_grafo)
            _ = input()
        case 2:
            vertice = input("Digite o nome do vertice: ")
            add_vertice(vertice)
        case 3:
            vertice1 = input("Digite o nome do primeiro vertice: ")
            vertice2 = input("Digite o nome do segundo vertice: ")
            if input("Sera uma aresta direcionado(s/n)") == "n":
                add_aresta(vertice1, vertice2)
            else:
                add_aresta_direcionada(vertice1, vertice2)
        case 4:
            vertice = input("Digite o nome do vertice: ")
            remove_vertice(vertice)
        case 5:
            vertice1 = input("Digite o nome do primeiro vertice: ")
            vertice2 = input("Digite o nome do segundo vertice: ")
            remove_aresta(vertice1, vertice2)
        case 6:
            vertice = input("Digite o nome do vertice: ")
            if vertice in lista_grafo:
                print(f"|{vertice}| = {len(lista_grafo[vertice])}")
            else:
                print("Vertice nao existe")
            _ = input()
        case 7:
            vertice1 = input("Digite o nome do primeiro vertice: ")
            vertice2 = input("Digite o nome do segundo vertice: ")
            if vertice2 in lista_grafo[vertice1]:
                print("Há adjacencia")
            else:
                print("Nao há adjacencia")
            _ = input()
        case 8:
            vertice = input("Digite o nome do vertice: ")
            print(lista_grafo[vertice])
            _ = input()
        case 9:
            vertice1 = input("Digite o nome do primeiro vertice: ")
            vertice2 = input("Digite o nome do segundo vertice: ")
            if checar_percurso(vertice1, vertice2):
                print("Há percurso")
            else:
                print("Nao há percurso")
            _ = input()

