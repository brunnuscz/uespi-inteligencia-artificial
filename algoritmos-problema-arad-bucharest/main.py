class Adjacente: # CRIA A CLASSE ADJACENTE
    def __init__(self, cidade, distancia): # METODO CONSTRUTOR
        # ATRIBUTOS DA CLASSE
        self.cidade = cidade
        self.distancia = distancia
        # NOVO ATRIBUTO
        self.distanciaAEstrela = self.cidade.distanciaObjetivo + self.distancia

class Cidade: # CRIANDO CLASSE CIDADE
    def __init__(self, nome, distanciaObjetivo): # CONSTRUTOR DA CLASSE
        # ATRIBUTOS DA CLASSE
        self.nome = nome
        self.visitado = False
        self.adjacentes = []
        self.distanciaObjetivo = distanciaObjetivo

    def addCidadeAdjacente(self, cidade): # METODO PRA ADICIONAR CIDADES ADJACENTES
        self.adjacentes.append(cidade)

class Mapa: # CRIANDO A CLASSE MAPA
    # MAPA OBJETIVO SAIR DE ARAD PARA BUCHAREST

    # CRIANDO CADA UMA DAS CLASSES
    arad = Cidade('Arad', 366)
    zerind = Cidade('Zerind', 374)
    oradea = Cidade('Oradea', 380)
    sibiu = Cidade('Sibiu', 253)
    timisoara = Cidade('Timisoara', 329)
    lugoj = Cidade('Lugoj', 244)
    mehadia = Cidade('Mehadia', 241)
    dobreta = Cidade('Dobreta', 242)
    craiova = Cidade('Craiova', 160)
    rimnicu = Cidade('Rimnicu', 193)
    fagaras = Cidade('Fagaras', 178)
    pitesti = Cidade('Pitesti', 98)
    bucharest = Cidade('Bucharest', 0)
    giurgiu = Cidade('Giurgiu', 77)

    # CRIANDO AS LIGAÇÕES ENTRE AS CLASSES DE IDA E DE VOLTA
    arad.addCidadeAdjacente(Adjacente(zerind, 75)) # CRIANDO UM OBJETIVO DA CLASSE ADJACENTE
    arad.addCidadeAdjacente(Adjacente(sibiu, 140))
    arad.addCidadeAdjacente(Adjacente(timisoara, 118))

    zerind.addCidadeAdjacente(Adjacente(arad, 75))
    zerind.addCidadeAdjacente(Adjacente(oradea, 71))

    oradea.addCidadeAdjacente(Adjacente(zerind, 71))
    oradea.addCidadeAdjacente(Adjacente(sibiu, 151))

    sibiu.addCidadeAdjacente(Adjacente(oradea, 151))
    sibiu.addCidadeAdjacente(Adjacente(arad, 140))
    sibiu.addCidadeAdjacente(Adjacente(fagaras, 99))
    sibiu.addCidadeAdjacente(Adjacente(rimnicu, 80))

    timisoara.addCidadeAdjacente(Adjacente(arad, 118))
    timisoara.addCidadeAdjacente(Adjacente(lugoj, 111))

    lugoj.addCidadeAdjacente(Adjacente(timisoara, 111))
    lugoj.addCidadeAdjacente(Adjacente(mehadia, 70))

    mehadia.addCidadeAdjacente(Adjacente(lugoj, 70))
    mehadia.addCidadeAdjacente(Adjacente(dobreta, 75))

    dobreta.addCidadeAdjacente(Adjacente(mehadia, 75))
    dobreta.addCidadeAdjacente(Adjacente(craiova, 120))

    craiova.addCidadeAdjacente(Adjacente(dobreta, 120))
    craiova.addCidadeAdjacente(Adjacente(pitesti, 138))
    craiova.addCidadeAdjacente(Adjacente(rimnicu, 146))

    rimnicu.addCidadeAdjacente(Adjacente(craiova, 146))
    rimnicu.addCidadeAdjacente(Adjacente(sibiu, 80))
    rimnicu.addCidadeAdjacente(Adjacente(pitesti, 97))

    fagaras.addCidadeAdjacente(Adjacente(sibiu, 99))
    fagaras.addCidadeAdjacente(Adjacente(bucharest, 211))

    pitesti.addCidadeAdjacente(Adjacente(rimnicu, 97))
    pitesti.addCidadeAdjacente(Adjacente(craiova, 138))
    pitesti.addCidadeAdjacente(Adjacente(bucharest, 101))

    bucharest.addCidadeAdjacente(Adjacente(fagaras, 211))
    bucharest.addCidadeAdjacente(Adjacente(pitesti, 101))
    bucharest.addCidadeAdjacente(Adjacente(giurgiu, 90))

class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0

    def enfileirar(self, cidade):
        if self.fim == self.tamanho - 1:
            self.fim = -1
        self.fim += 1
        self.cidades[self.fim] = cidade
        self.numeroElementos += 1

    def desinfileirar(self):

        temp = self.cidades[self.inicio]
        self.inicio += 1
        if self.inicio == self.tamanho:
            self.inicio = 0
        self.numeroElementos -= 1
        return temp

    def getPrimeiro(self):
        return self.cidades[self.inicio]

    def filaVazia(self):
        return self.numeroElementos == 0

    def filaCheia(self):
        return self.numeroElementos == self.tamanho

class Pilha: # CRIANDO A CLASSE PILHA
    def __init__(self, tamanho): # CONSTRUTOR DA CLASSE
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.topo = -1

    def empilhar(self, cidade): # METODO PRA ADICIONA UMA CIDADE NA PILHA
        if not Pilha.pilhaCheia(self):
            self.topo += 1
            self.cidades[self.topo] = cidade
        else:
            print("Pilha esta cheia")

    def desempilhar(self): # METODO PARA DESENPILHAR UMA CIDADE DA PILHA
        if not Pilha.pilhaVazia(self): # VERIFICA SE A PILHA NÃO ESTÁ VAZIA
            temporario = self.cidades[self.topo]
            self.topo -= 1 # RETORNA A CIDADE TIRADA DA PILHA
            return temporario
        else:
            print("Pilha esta vazia")
            return None

    def getTopo(self):
        return self.cidades[self.topo]

    def pilhaVazia(self):
        return (self.topo == -1)

    def pilhaCheia(self):
        return (self.topo == self.tamanho - 1)

class VetorOrdenado: # CRIANDO CLASSE DO VETOR
    def __init__(self, tamanho):
        self.numeroElementos = 0
        self.cidades = [None] * tamanho

    def inserir(self, cidade):
        if self.numeroElementos == 0:
            self.cidades[0] = cidade
            self.numeroElementos = 1
            return

        posicao = 0
        i = 0
        while i < self.numeroElementos:
            if cidade.distanciaObjetivo > self.cidades[posicao].distanciaObjetivo:
                posicao += 1
            i += 1

        for k in range(self.numeroElementos, posicao, -1):
            self.cidades[k] = self.cidades[k - 1]

        self.cidades[posicao] = cidade
        self.numeroElementos = self.numeroElementos + 1

    def getPrimeiro(self):
        return self.cidades[0] # BUSCA A CIDADE DE MENOR CUSTO

    def mostrar(self):
        for i in range(0, self.numeroElementos): # PERCORRE AS CIDADES DO VETOR
            print("{} - {}".format(self.cidades[i].nome, self.cidades[i].distanciaObjetivo))

class VetorOrdenadoAdjacente:
    def __init__(self, tamanho):
        self.numeroElementos = 0
        self.adjacentes = [None] * tamanho

    def inserir(self, adjacente):
        if self.numeroElementos == 0:
            self.adjacentes[0] = adjacente
            self.numeroElementos = 1
            return

        posicao = 0
        i = 0
        while i < self.numeroElementos:
            if adjacente.distanciaAEstrela > self.adjacentes[posicao].distanciaAEstrela:
                posicao += 1
            i += 1

        for k in range(self.numeroElementos, posicao, -1):
            self.adjacentes[k] = self.adjacentes[k - 1]

        self.adjacentes[posicao] = adjacente
        self.numeroElementos = self.numeroElementos + 1

    def getPrimeiro(self):
        return self.adjacentes[0].cidade

    def mostrar(self):
        for i in range(0, self.numeroElementos):
            print("{} - {}".format(self.adjacentes[i].cidade.nome, self.adjacentes[i].distanciaAEstrela))

class BuscaGulosa: # CRIA A CLASSE DE BUSCA GULOSA
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False

    def buscar(self, atual): # CIDADE ATUAL COMO PARAMETRO
        print("\nAtual: {}".format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            self.achou = True
            print("\n Chegamos ao objetivo")
        else:
            self.fronteira = VetorOrdenado(len(atual.adjacentes))

            for i in atual.adjacentes:
                if i.cidade.visitado == False:
                    i.cidade.visitado = True # MARCADO COMO VISITADO
                    self.fronteira.inserir(i.cidade) # ADICIONA ADJACENTE AO VETOR
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None: # SE NÃO TIVER VAZIO

                BuscaGulosa.buscar(self, self.fronteira.getPrimeiro()) # CHAMA A NOVA CIDADE A SER EXPANDIDA

class BuscaAEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False

    def buscar(self, atual):
        print("\nAtual: {}".format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            print("Objetivo {} foi alcançado. ".format(self.objetivo.nome))
            self.achou = True
        else:
            self.fronteira = VetorOrdenadoAdjacente(len(atual.adjacentes))
            # PERCORRE AS CIDADES
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    # ADICIONA O ADJACENTE AO VETOR
                    self.fronteira.inserir(a)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                BuscaAEstrela.buscar(self, self.fronteira.getPrimeiro())

class BuscaEmProfundidade:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True # MARCADO COMO VISITADA
        self.objetivo = objetivo
        self.fronteira = Pilha(1000) # ARMAZENA AS CIDADES QUE SERÃO VISITADAS
        self.fronteira.empilhar(inicio) # EMPILHA AS CIDADES DE INICIO
        self.achou = False

    def buscar(self):
        topo = self.fronteira.getTopo() # BUSCA A CIDADE DO TOPO DA PILHA

        if topo == self.objetivo: # VERIFICA SE É A CIDADE OBJETIVO
            self.achou = True
            print("Objetivo {}".format(self.objetivo.nome), "foi alcançado apartir de {}".format(self.inicio.nome))
        else: # SE NÃO ACHAR, EXECUTA A BUSCA
            print("Topo: {}".format(topo.nome))
            for adjacente in topo.adjacentes:
                if self.achou == False:
                    print("Já foi visitado? ", adjacente.cidade.nome)
                    if adjacente.cidade.visitado == False:
                        adjacente.cidade.visitado == True # MARCADA COMO VISITADA
                        self.fronteira.empilhar(adjacente.cidade) # EMPILHA A CIDADE
                        BuscaEmProfundidade.buscar(self) # CHAMA NOVAMENTE O MÉTODO BUSCAR
        print("Desempilhou: {}".format(self.fronteira.desempilhar().nome)) # APÓS ENCONTRAR A IDADE OBJEITVO É DESEMPILHADO TODAS

class BuscaEmProfundidadeVisitados:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        # fronteira armazena pilha de cidades que serão visitadas
        self.fronteira = Pilha(1000)
        self.fronteira.empilhar(inicio)
        self.achou = False

    def buscar(self):
        topo = self.fronteira.getTopo()
        print("Topo: {}".format(topo.nome))

        if topo == self.objetivo:
            print("Objetivo {}".format(self.objetivo.nome), "foi alcançado apartir de {}".format(self.inicio.nome))
            self.achou = True
        else:
            for adjacente in topo.adjacentes:
                if self.achou == False:
                    print("Verificando se ja visitado: {}".format(adjacente.cidade.nome))
                    if adjacente.cidade.visitado == False:
                        adjacente.cidade.visitado = True
                        self.fronteira.empilhar(adjacente.cidade)
                        BuscaEmProfundidadeVisitados.buscar(self)
        # print("Desempilhou: {}" .format(self.fronteira.desempilhar().nome))

class BuscaLargura:

    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Fila(10000)
        self.fronteira.enfileirar(inicio)
        self.achou = False

    def buscar(self):

        print("Objetivo: {} ".format(self.objetivo.nome))
        primeiro = self.fronteira.getPrimeiro()
        print("primeiro: {}".format(primeiro.nome))

        if primeiro == self.objetivo:
            print("Objetivo {}".format(self.objetivo.nome), "foi alcançado apartir de {}".format(self.inicio.nome))
            self.achou = True
        else:
            temp = self.fronteira.desinfileirar()
            print("Desinfileirou: {}".format(temp.nome))
            for a in primeiro.adjacentes:
                print("Verificando se já visitado: {}".format(a.cidade.nome))
                if a.cidade.visitado == False:
                    self.fronteira.enfileirar(a.cidade)
                    a.cidade.visitado = True
            if self.fronteira.numeroElementos > 0:
                BuscaLargura.buscar(self)
            else:
                print("Objetivo: ", format(self.objetivo.nome), "foi achado apartir de ", format(primeiro.nome))

# BUSCA GULOSA
# mapa = Mapa()
# gulosa = BuscaGulosa(mapa.bucharest)
# gulosa.buscar(mapa.arad)

# BUSCA A*
# mapa = Mapa()
# aestrela = BuscaAEstrela(mapa.bucharest)
# aestrela.buscar(mapa.arad)

# BUSCA EM PROFUNDIDADE VISITADOS
# mapa = Mapa()
# profundidade = BuscaEmProfundidadeVisitados(mapa.arad, mapa.bucharest)
# profundidade.buscar()

# BUSCA EM LARGURA
# mapa = Mapa()
# largura = BuscaLargura(mapa.arad, mapa.bucharest)
# largura.buscar()

# BUSCA EM PROFUNDIDADE
# mapa = Mapa()
# profundidade = BuscaEmProfundidade(mapa.bucharest, mapa.arad)
# profundidade.buscar()



