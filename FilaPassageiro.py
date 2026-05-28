class NoFila:
    def __init__(self, passageiro):
        self.passageiro = passageiro
        self.proximo = None


class FilaPassageiro:

    def __init__(self):
        self.frente = None
        self.fim = None

    def adicionar_passageiro(self, passageiro):
        novo_no = NoFila(passageiro)

        if self.frente is None:
            self.frente = novo_no
            self.fim = novo_no
            return

        self.fim.proximo = novo_no
        self.fim = novo_no

    def remover_primeiro(self):

        if self.frente is None:
            return None

        passageiro = self.frente.passageiro
        self.frente = self.frente.proximo

        if self.frente is None:
            self.fim = None

        return passageiro

    def esta_vazia(self):
        return self.frente is None

    def __str__(self):

        atual = self.frente
        passageiros = []

        while atual is not None:
            passageiros.append(str(atual.passageiro))
            atual = atual.proximo

        return " -> ".join(passageiros) if passageiros else "Fila vazia"