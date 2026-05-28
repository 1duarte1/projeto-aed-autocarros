from FilaPassageiro import FilaPassageiro


class Paragem:
    """
    Classe que representa uma paragem de autocarro.
    """

    def __init__(self, nome: str):

        # Nome da paragem
        self.nome = nome

        # Fila dinâmica de passageiros
        self.fila_passageiros = FilaPassageiro()

        # Ponteiro para a próxima paragem
        self.next = None

    def adicionar_passageiro(self, passageiro):
        """
        Adiciona um passageiro à fila de espera.
        """

        self.fila_passageiros.adicionar_passageiro(passageiro)

    def remover_passageiro(self):
        """
        Remove um passageiro da frente da fila.
        """

        return self.fila_passageiros.remover_primeiro()

    def num_passageiros(self):
        """
        Devolve o número de passageiros na fila.
        """

        atual = self.fila_passageiros.frente

        contador = 0

        while atual is not None:
            contador += 1
            atual = atual.proximo

        return contador

    def __str__(self):
        
        return f"{self.nome} ({self.num_passageiros()} passageiros)"