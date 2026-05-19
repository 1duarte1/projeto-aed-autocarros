class Linha:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
    
    def esta_vazia(self) -> bool:
        return self.inicio is None
    
    def inserir_paragem(self, nome: str) -> bool:
        """Insere uma nova paragem no final da lista"""
        nova_paragem = Paragem(nome)
        
        if self.esta_vazia():
            self.inicio = nova_paragem
        else:
            atual = self.inicio
            while atual.proxima is not None:
                # Verifica se a paragem já existe
                if atual.nome == nome:
                    print(f"Paragem '{nome}' já existe!")
                    return False
                atual = atual.proxima
            
            # Verifica a última paragem
            if atual.nome == nome:
                print(f"Paragem '{nome}' já existe!")
                return False
            
            atual.proxima = nova_paragem
        
        self.tamanho += 1
        print(f"Paragem '{nome}' adicionada com sucesso!")
        return True
    
    def remover_paragem(self, nome: str) -> bool:
        """Remove uma paragem pelo nome"""
        if self.esta_vazia():
            print("Lista vazia!")
            return False
        
        # Caso especial: remoção do início
        if self.inicio.nome == nome:
            self.inicio = self.inicio.proxima
            self.tamanho -= 1
            print(f"Paragem '{nome}' removida!")
            return True
        
        # Percorre a lista procurando a paragem
        atual = self.inicio
        while atual.proxima is not None:
            if atual.proxima.nome == nome:
                atual.proxima = atual.proxima.proxima
                self.tamanho -= 1
                print(f"Paragem '{nome}' removida!")
                return True
            atual = atual.proxima
        
        print(f"Paragem '{nome}' não encontrada!")
        return False
    
    def buscar_paragem(self, nome: str) -> paragem | None:
        """Busca uma paragem pelo nome"""
        atual = self.inicio
        while atual is not None:
            if atual.nome == nome:
                return atual
            atual = atual.proxima
        return None
    
    def listar_percurso(self) -> None:
        """Lista todas as paragens do percurso"""
        print("\n=== Percurso da Linha ===")
        if self.esta_vazia():
            print("Nenhuma paragem cadastrada.")
            return
        
        atual = self.inicio
        contador = 1
        while atual is not None:
            print(f"{contador}. {atual}")
            atual.mostrar_fila()
            atual = atual.proxima
            contador += 1
        
        print(f"\nTotal de paragens: {self.tamanho}")
    
    def get_todas_paragens(self) -> list[Paragem]:
        """Retorna uma lista com todas as paragens"""
        paragens = []
        atual = self.inicio
        while atual is not None:
            paragens.append(atual)
            atual = atual.proxima
        return paragens