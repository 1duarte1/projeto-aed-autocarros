class Paragem:

    def __init__(self, nome: str):
        self.nome = nome
        self.passageiros_em_espera = []   # Fila FIFO
        self.proxima = None               # Próxima paragem (lista ligada)

    def adicionar_passageiro(self, nome: str) -> None:
        """Adiciona um passageiro à fila"""
        self.passageiros_em_espera.append(nome)

    def remover_passageiro(self) -> str | None:
        """Remove o primeiro passageiro da fila"""
        if self.passageiros_em_espera:
            return self.passageiros_em_espera.pop(0)
        return None

    def get_numero_passageiros(self) -> int:
        """Retorna o número de passageiros em espera"""
        return len(self.passageiros_em_espera)

    def mostrar_fila(self) -> None:
        """Mostra todos os passageiros da fila"""
        print(f"\nPassageiros na paragem '{self.nome}':")

        if not self.passageiros_em_espera:
            print("  Nenhum passageiro.")
        else:
            for passageiro in self.passageiros_em_espera:
                print(f"  - {passageiro}")

    def __str__(self) -> str:
        return f"Paragem: {self.nome} | Passageiros: {self.get_numero_passageiros()}"