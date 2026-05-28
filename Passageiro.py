class Passageiro:

    def __init__(self, nome, destino):
        self.nome = nome
        self.destino = destino

    def __str__(self):
        return f"{self.nome} -> {self.destino}"