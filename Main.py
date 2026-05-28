from LinhaAutocarro import Linha
from Passageiro import Passageiro
from Autocarro import Autocarro


def main():

    linha = None
    autocarro = Autocarro()

    while True:

        print("\n===== SIMULADOR LINHA DE AUTOCARROS =====")
        print("1. Criar linha de autocarro")
        print("2. Adicionar paragem")
        print("3. Remover paragem")
        print("4. Adicionar passageiro a uma paragem")
        print("5. Simular viagem completa")
        print("6. Mostrar estado da linha")
        print("0. Sair")

        opcao = input("Escolhe uma opção: ")

        # 1. Criar linha
        if opcao == "1":
            linha = Linha()
            print("Linha criada com sucesso!")

        # 2. Adicionar paragem
        elif opcao == "2":

            if linha is None:
                print("Cria primeiro a linha!")
                continue

            nome = input("Nome da paragem: ")
            linha.inserir_paragem(nome)
            print("Paragem adicionada!")

        # 3. Remover paragem
        elif opcao == "3":

            if linha is None:
                print("Cria primeiro a linha!")
                continue

            nome = input("Nome da paragem a remover: ")

            if linha.remover_paragem(nome):
                print("Paragem removida!")
            else:
                print("Paragem não encontrada.")

        # 4. Adicionar passageiro
        elif opcao == "4":

            if linha is None:
                print("Cria primeiro a linha!")
                continue

            nome_paragem = input("Paragem onde o passageiro espera: ")
            nome_passageiro = input("Nome do passageiro: ")
            destino = input("Destino do passageiro: ")

            atual = linha.cabeca
            encontrado = False

            while atual is not None:

                if atual.nome == nome_paragem:

                    p = Passageiro(nome_passageiro, destino)
                    atual.adicionar_passageiro(p)

                    print("Passageiro adicionado!")
                    encontrado = True
                    break

                atual = atual.next

            if not encontrado:
                print("Paragem não encontrada.")

        # 5. Simular viagem
        elif opcao == "5":

            if linha is None:
                print("Cria primeiro a linha!")
                continue

            if linha.cabeca is None:
                print("Linha vazia!")
                continue

            autocarro.simular_viagem(linha)

        # 6. Mostrar linha
        elif opcao == "6":

            if linha is None:
                print("Cria primeiro a linha!")
                continue

            linha.listar_percurso()

        # 0. Sair
        elif opcao == "0":
            print("A sair do programa...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()