from Autocarro import Autocarro
from Ordenecao import Ordenacao
from paragem import Paragem


def criar_linha():
    return []


def mostrar_linha(linha):
    print("\n=== LINHA DE AUTOCARRO ===")
    for i, p in enumerate(linha):
        print(f"{i + 1}. {p}")


def encontrar_paragem(linha, nome):
    for p in linha:
        if p.nome.lower() == nome.lower():
            return p
    return None


def main():

    linha = criar_linha()
    autocarro = Autocarro(3)

    while True:

        print("\n==MENU ==")
        print("1. Adicionar paragem")
        print("2. Remover paragem")
        print("3. Adicionar passageiro a paragem")
        print("4. Simular chegada do autocarro")
        print("5. Ordenar paragens por nome")
        print("6. Ordenar paragens por passageiros")
        print("7. Mostrar estado da linha")
        print("0. Sair")

        opcao = input("Escolha: ")

        # 1
        if opcao == "1":
            nome = input("Nome da paragem: ")
            linha.append(Paragem(nome))
            print("Paragem adicionada.")

        # 2 - REMOVER PARAGEM (CORRIGIDO)
        elif opcao == "2":

            if len(linha) == 0:
                print("Não existem paragens ainda.")

            else:
                print("\nParagens disponíveis:")
                for p in linha:
                    print("-", p.nome)

                nome = input("\nNome da paragem a remover: ")
                paragem = encontrar_paragem(linha, nome)

                if paragem:
                    linha.remove(paragem)
                    print("Paragem removida.")
                else:
                    print("Paragem não encontrada.")

        # 3
        elif opcao == "3":
            nome_paragem = input("Nome da paragem: ")
            nome_passageiro = input("Nome do passageiro: ")

            paragem = encontrar_paragem(linha, nome_paragem)

            if paragem:
                paragem.adicionar_passageiro(nome_passageiro)
            else:
                print("Paragem não encontrada.")

        # 4
        elif opcao == "4":
            nome_paragem = input("Paragem atual: ")

            paragem = encontrar_paragem(linha, nome_paragem)

            if paragem:
                print("\nChegou o autocarro!")

                passageiro = paragem.remover_passageiro()

                if passageiro:
                    autocarro.embarcar(passageiro)
                else:
                    print("Não há passageiros na paragem.")

                autocarro.mostrar_passageiros()

            else:
                print("Paragem não encontrada.")

        # 5
        elif opcao == "5":
            Ordenacao.bubble_sort_nome(linha)
            print("Paragens ordenadas por nome.")

        # 6
        elif opcao == "6":
            Ordenacao.insertion_sort_passageiros(linha)
            print("Paragens ordenadas por passageiros.")

        # 7
        elif opcao == "7":
            mostrar_linha(linha)

            print("\n=== AUTOCARRO ===")
            autocarro.mostrar_passageiros()

        # 0
        elif opcao == "0":
            print("A sair...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()