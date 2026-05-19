class Grafo:
    def __init__(self):
        self.paragens = {}  # Dicionário de adjacência
        self.peso = {}      # Pesos das arestas
    
    def adicionar_paragem(self, nome: str) -> None:
        if nome not in self.paragens:
            self.paragens[nome] = []
            print(f"Paragem '{nome}' adicionada ao grafo.")
    
    def adicionar_ligacao(self, origem: str, destino: str, peso: int = 1) -> None:
        """Adiciona uma ligação entre duas paragens"""
        # Cria as paragens se não existirem
        self.adicionar_paragem(origem)
        self.adicionar_paragem(destino)
        
        # Adiciona a aresta (grafo não dirigido)
        if destino not in self.paragens[origem]:
            self.paragens[origem].append(destino)
        if origem not in self.paragens[destino]:
            self.paragens[destino].append(origem)
        
        # Armazena o peso
        self.peso[(origem, destino)] = peso
        self.peso[(destino, origem)] = peso
        
        print(f"Ligação '{origem} <-> {destino}' criada.")
    
    def mostrar_grafo(self) -> None:
        """Mostra todas as ligações do grafo"""
        print("\n=== Rede de Paragens ===")
        for paragem, vizinhos in self.paragens.items():
            print(f"{paragem} -> {', '.join(vizinhos)}")
    
    # algoritmos de busca em largura (BFS)
    def encontrar_caminho_bfs(self, inicio: str, destino: str) -> list[str] | None:
        """Encontra o caminho entre duas paragens usando BFS"""
        if inicio not in self.paragens or destino not in self.paragens:
            return None
        
        # Queue para BFS: [(paragem_atual, caminho)]
        fila = [(inicio, [inicio])]
        visitados = {inicio}
        
        while fila:
            atual, caminho = fila.pop(0)
            
            if atual == destino:
                return caminho
            
            for vizinho in self.paragens[atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    novo_caminho = caminho + [vizinho]
                    fila.append((vizinho, novo_caminho))
        
        return None  # Não há caminho
    
    # Algoritmo de Dijkstra para caminho mais curto
    def dijkstra(self, inicio: str, destino: str) -> tuple[list[str], int]:
        """Encontra o caminho mais curto entre duas paragens"""
        import heapq
        
        # Distâncias e caminhos
        distancias = {p: float('inf') for p in self.paragens}
        caminhos = {p: [] for p in self.paragens}
        distancias[inicio] = 0
        caminhos[inicio] = [inicio]
        
        # Heap: (distância, paragem, caminho)
        heap = [(0, inicio, [inicio])]
        visitados = set()
        
        while heap:
            dist_atual, atual, caminho_atual = heapq.heappop(heap)
            
            if atual in visitados:
                continue
            
            visitados.add(atual)
            
            if atual == destino:
                return caminho_atual, dist_atual
            
            for vizinho in self.paragens[atual]:
                if vizinho not in visitados:
                    peso = self.peso.get((atual, vizinho), 1)
                    nova_dist = dist_atual + peso
                    
                    if nova_dist < distancias[vizinho]:
                        distancias[vizinho] = nova_dist
                        novo_caminho = caminho_atual + [vizinho]
                        heapq.heappush(heap, (nova_dist, vizinho, novo_caminho))
        
        return [], float('inf')