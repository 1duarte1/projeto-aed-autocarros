from Paragem import Paragem

class Linha:
    """
  Classe que representa uma linha 
  de autocarro com lista ligada de paragens.

    """

    def __init__(self):
        # Referência para a primeira paragem
        self.cabeca = None

    def inserir_paragem(self, nome):
        """
        Insere uma nova paragem no fim da linha.
        """

        nova = Paragem(nome)

        # Se a linha estiver vazia
        if self.cabeca is None:
            self.cabeca = nova
            return

        # Percorrer até à última paragem
        atual = self.cabeca

        while atual.next is not None:
            atual = atual.next

        # Ligar a nova paragem ao fim
        atual.next = nova

    def remover_paragem(self, nome):
        """
        Remove uma paragem pelo nome.
        """

        atual = self.cabeca
        anterior = None

        while atual is not None:

            if atual.nome == nome:

                # Remover a primeira paragem
                if anterior is None:
                    self.cabeca = atual.next

                # Remover uma paragem do meio ou do fim
                else:
                    anterior.next = atual.next

                return True

            anterior = atual
            atual = atual.next

        return False

    def listar_percurso(self):
        """
        Mostra todas as paragens da linha.
        """

        atual = self.cabeca

        if atual is None:
            print("A linha não possui paragens.")
            return

        while atual is not None:
            print(atual.nome)
            atual = atual.next

    def simular_viagem(self):
        """
        Simula a viagem do autocarro pelas paragens da linha.
        """

        atual = self.cabeca

        if atual is None:
            print("Não existem paragens na linha.")
            return

        print("=== Início da viagem ===")

        while atual is not None:
            print(f"Autocarro chegou à paragem: {atual.nome}")

        
            atual = atual.next

        print("=== Fim da viagem ===")