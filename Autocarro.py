class Autocarro:
    """
    Classe que representa um autocarro.
    """

    def __init__(self, capacidade_maxima=50):

        # Número máximo de passageiros
        self.capacidade_maxima = capacidade_maxima

        # Lista de passageiros dentro do autocarro
        self.passageiros_a_bordo = []

        # Paragem atual
        self.paragem_atual = None

    def entrar_passageiro(self, passageiro):
        """
        Adiciona um passageiro ao autocarro
        se existir espaço disponível.
        """

        if len(self.passageiros_a_bordo) >= self.capacidade_maxima:
            print("O autocarro está cheio.")
            return False

        self.passageiros_a_bordo.append(passageiro)

        print(f"{passageiro.nome} entrou no autocarro.")

        return True

    def embarcar_passageiros(self):
        """
        Retira passageiros da fila da paragem
        e coloca-os no autocarro enquanto houver espaço.
        """

        if self.paragem_atual is None:
            print("O autocarro não está numa paragem.")
            return

        fila = self.paragem_atual.fila_passageiros

        while (
            not fila.esta_vazia()
            and len(self.passageiros_a_bordo) < self.capacidade_maxima
        ):

            passageiro = fila.remover_primeiro()

            self.entrar_passageiro(passageiro)

    def desembarcar_passageiros(self, nome_paragem):
        """
        Remove passageiros cujo destino
        seja a paragem atual.
        """

        passageiros_saida = []

        for passageiro in self.passageiros_a_bordo:

            if passageiro.destino == nome_paragem:
                passageiros_saida.append(passageiro)

        for passageiro in passageiros_saida:

            self.passageiros_a_bordo.remove(passageiro)

            print(f"{passageiro.nome} saiu do autocarro.")

    def definir_paragem_atual(self, paragem):
        """
        Define a paragem atual do autocarro.
        """

        self.paragem_atual = paragem

    def listar_passageiros(self):
        """
        Mostra os passageiros dentro do autocarro.
        """

        if len(self.passageiros_a_bordo) == 0:
            print("Não existem passageiros a bordo.")
            return

        for passageiro in self.passageiros_a_bordo:
            print(passageiro)

    def simular_viagem(self, linha):
        """
        Percorre todas as paragens da linha.
        """

        atual = linha.cabeca

        while atual is not None:

            # Atualizar a paragem atual
            self.definir_paragem_atual(atual)

            print(f"\n=== PARAGEM: {atual.nome} ===")

            # Passageiros saem
            self.desembarcar_passageiros(atual.nome)

            # Passageiros entram
            self.embarcar_passageiros()

            # Mostrar passageiros atuais
            print("\nPassageiros no autocarro:")

            self.listar_passageiros()

            # Avançar para a próxima paragem
            atual = atual.next

        print("\n=== Fim da linha ===")