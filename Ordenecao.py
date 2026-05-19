class Ordenacao:

    @staticmethod
    def bubble_sort_nome(paragens):
        """Ordena paragens por nome usando Bubble Sort"""

        n = len(paragens)

        for i in range(n):
            for j in range(0, n - i - 1):

                if paragens[j].nome > paragens[j + 1].nome:
                    paragens[j], paragens[j + 1] = paragens[j + 1], paragens[j]

        return paragens

    @staticmethod
    def insertion_sort_passageiros(paragens):
        """Ordena paragens por número de passageiros usando Insertion Sort"""

        for i in range(1, len(paragens)):

            atual = paragens[i]
            j = i - 1

            while j >= 0 and (
                paragens[j].get_numero_passageiros()
                > atual.get_numero_passageiros()
            ):

                paragens[j + 1] = paragens[j]
                j -= 1

            paragens[j + 1] = atual

        return paragens

    @staticmethod
    def selection_sort_nome(paragens):
        """Ordena paragens por nome usando Selection Sort"""

        n = len(paragens)

        for i in range(n):

            menor = i

            for j in range(i + 1, n):

                if paragens[j].nome < paragens[menor].nome:
                    menor = j

            paragens[i], paragens[menor] = paragens[menor], paragens[i]

        return paragens