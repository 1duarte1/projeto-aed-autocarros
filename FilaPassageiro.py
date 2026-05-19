class FilaPassageiros:

    def __init__(self):
        self.fila = []

    def enfileirar(self, nome: str) -> None:
        """Adiciona passageiro ao final da fila"""

        self.fila.append(nome)
        print(f"Passageiro '{nome}' adicionado à fila.")

    def desenfileirar(self) -> str | None:
        """Remove e retorna o primeiro passageiro"""

        if self.esta_vazia():
            return None

        return self.fila.pop(0)

    def primeiro(self) -> str | None:
        """Retorna o primeiro passageiro sem remover"""

        if self.esta_vazia():
            return None

        return self.fila[0]

    def esta_vazia(self) -> bool:
        return len(self.fila) == 0

    def tamanho(self) -> int:
        return len(self.fila)

    def mostrar(self) -> None:
        """Mostra todos os passageiros"""

        print("Fila de passageiros:")

        if self.esta_vazia():
            print("  Vazia")
        else:
            for p in self.fila:
                print(f"  - {p}")

    def __str__(self) -> str:
        return ", ".join(self.fila)