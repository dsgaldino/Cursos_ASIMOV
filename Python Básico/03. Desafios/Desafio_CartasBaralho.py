# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:

# gerar_baralho -> retorna um baralho novo. Parâmetros da função
# definem quantas cópias retornar (1 baralho, 2 baralhos, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado
# antes de ser retornado.

# mostrar_baralho -> exibe a quantidade de cartas no baralho e
# mostra quais são.

# dar_as_cartas -> distribui as cartas do baralho entre X
# jogadores, de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de
# cada jogador e mostra quais são.

# A partir dessas funções, o código deve:
# - gerar o baralho e exibi-lo
# - dar as cartas para os jogadores
# - exibir o baralho após as cartas terem sido distribuídas
# - exibir a mão de cada jogador

# DICA: utilize os símbolos ♠ ♥ ♦ ♣ para representar os naipes.
# DICA: utilize a função random.shuffle (módulo random) para embaralhar.

import random

def gerar_baralho(quantidade, coringa, embaralhamento):
    naipes = ["♠", "♥", "♦", "♣"]
    valores = ["A"] + list(map(str, range(2, 11))) + ["J", "Q", "K"]
    baralho = []

    """
        Aqui cria os baralhos por naipe e não por valores

        Exemplos da criação do baralho:

        Correta: A♠, 2♠, 3♠, 4♠
        Errada: A♠, A♥ , A♦, A♣

    """
    for _ in range(quantidade):
        for naipe in naipes:
            for valor in valores:
                baralho.append(valor + naipe)

        if coringa:
            baralho.append("Joker★")
            baralho.append("Joker☆")

    if embaralhamento:
        random.shuffle(baralho)

    return baralho

def dar_as_cartas(baralho, num_jogadores, num_cartas):
    jogadores = [[] for _ in range(num_jogadores)]

    """
        Forma da distruibuição de cartas:

            Primeiro carta para A
            Primeiro carta para B
            Segunda carta para A
            Segunda carta para B

        E assim sucessivamente até completarem as mãos.

    """
    for _ in range(num_cartas):
        for jogador in jogadores:
            if len(baralho) > 0:
                jogador.append(baralho.pop(0))
    return jogadores

def mostrar_baralho(baralho):
    print(f"\nO baralho tem {len(baralho)} cartas:")

    # Imprime as cartas, quebrando a linha a cada 13 cartas para melhor visualização
    for i, carta in enumerate(baralho, 1):
        print(carta, end=' ')
        if i % 13 == 0:
            print()  # quebra de linha a cada 13 cartas
    print()  # quebra de linha final

def mostrar_jogadores(jogadores):
    for i, mao in enumerate(jogadores, 1):
        # imprime o título e as cartas na mesma linha
        print(f"Jogador {i} tem {len(mao)} cartas: {' '.join(mao)}\n")


def ler_int_positivo(prompt):
    while True:
        try:
            valor = int(input(prompt))
            if valor < 1:
                print("Por favor, informe um número inteiro positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def ler_sn(prompt):
    while True:
        resposta = input(prompt).lower()
        if resposta in ('s', 'n'):
            return resposta == 's'
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

def menu():
    print("Configuração do Baralho e Jogadores")

    quantidade = ler_int_positivo("Quantos baralhos deseja usar? (ex: 1): ")
    coringa = ler_sn("Incluir coringas? (s/n): ")
    embaralhamento = ler_sn("Embaralhar o baralho? (s/n): ")
    num_jogadores = ler_int_positivo("Número de jogadores: ")
    num_cartas = ler_int_positivo("Cartas por jogador: ")

    return quantidade, coringa, embaralhamento, num_jogadores, num_cartas

def main():
    quantidade, coringa, embaralhamento, num_jogadores, num_cartas = menu()

    baralho = gerar_baralho(quantidade, coringa, embaralhamento)

    print("\nBaralho Inicial:")
    mostrar_baralho(baralho)

    jogadores = dar_as_cartas(baralho, num_jogadores, num_cartas)

    print("\nBaralho após distribuir cartas:")
    mostrar_baralho(baralho)

    print("\nCartas dos jogadores:")
    mostrar_jogadores(jogadores)


if __name__ == "__main__":
    main()


