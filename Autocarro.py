class Autocarro:

    def __init__(self, capacidade_maxima: int = 50):
        self.capacidade_maxima = capacidade_maxima
        self.passageiros = []   # Passageiros dentro do autocarro

    def embarcar(self, nome: str) -> bool:
        """Adiciona passageiro ao autocarro"""

        if len(self.passageiros) < self.capacidade_maxima:
            self.passageiros.append(nome)

            print(f"{nome} entrou no autocarro.")
            return True

        print("Autocarro cheio!")
        return False

    def desembarcar(self, nome: str) -> bool:
        """Remove passageiro do autocarro"""

        if nome in self.passageiros:
            self.passageiros.remove(nome)

            print(f"{nome} saiu do autocarro.")
            return True

        print(f"Passageiro '{nome}' não encontrado no autocarro.")
        return False

    def get_numero_passageiros(self) -> int:
        """Retorna o número de passageiros"""
        return len(self.passageiros)

    def lugares_disponiveis(self) -> int:
        """Retorna lugares disponíveis"""
        return self.capacidade_maxima - len(self.passageiros)

    def mostrar_passageiros(self) -> None:
        """Mostra passageiros no autocarro"""

        print("\n=== Passageiros no Autocarro ===")

        if not self.passageiros:
            print("Nenhum passageiro.")
        else:
            for p in self.passageiros:
                print(f"- {p}")

    def __str__(self) -> str:
        return f"Autocarro | Passageiros: {self.get_numero_passageiros()}/{self.capacidade_maxima}"