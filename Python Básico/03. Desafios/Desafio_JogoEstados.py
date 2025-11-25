# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.

#Critério adicionados ao desafio

# Pontuação
# O jogador terá 3 tentativas para acertar a capital do estado.
# Se acertar na primeira tentativa ganha 5 pontos
# Se acertar na segunda tentativa ganha 3 pontos
# Se acertar na terceira tentativa ganha 1 ponto
# Se errar ganha 0 pontos

# Mostrar um ranking com o top 5 maiores pontuadores do Jogo

import random

estados_capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

# Função para obter o nome do jogador, limitado a até 10 caracteres.
def obter_nome_jogador():
    while True:
        nome = input("Digite seu nome (até 10 caracteres): ").strip()
        if 0 < len(nome) <= 10:
            return nome
        print("Nome inválido. Por favor, digite até 10 caracteres.")

# Função principal do jogo.
# Pergunta as capitais dos estados, com até 3 tentativas por estado.
# Considera maiúsculas/minúsculas iguais, mas exige que o jogador digite os acentos corretamente.
# Permite encerrar o jogo a qualquer momento digitando 'sair'.
# Retorna o nome do jogador, o score acumulado e o total de estados respondidos.

def jogar(estados_capitais):
    import random
    print("\n=== Instruções ===")
    print("Digite o nome da capital do estado.")
    print("Letras maiúsculas e minúsculas serão consideradas iguais.")
    print("Os acentos devem ser digitados corretamente para pontuar integralmente.")
    print("Caso queira encerrar o jogo a qualquer momento, digite 'sair'.\n")

    nome_jogador = obter_nome_jogador()
    score = 0
    total_respondidos = 0

    # Lista com pares (estado, capital) embaralhada
    lista_estados = list(estados_capitais.items())
    random.shuffle(lista_estados)

    for estado, capital_correta in lista_estados:
        tentativas = 0
        acertou = False

        while tentativas < 3 and not acertou:
            tentativa = input(f"Qual a capital do estado {estado}? ").strip()
            if tentativa.lower() == 'sair':
                print("Você escolheu encerrar o jogo.\n")
                return nome_jogador, score, total_respondidos

            tentativas += 1
            
            if tentativa.lower() == capital_correta.lower():
                pontos = 5 if tentativas == 1 else 3 if tentativas == 2 else 1
                print(f"Acertou! Você ganhou {pontos} pontos.\n")
                score += pontos
                acertou = True
            else:
                if tentativas < 3:
                    print("Errado! Tente novamente.")
                else:
                    print(f"Errado! A capital correta é {capital_correta}.\n")

        total_respondidos += 1

    return nome_jogador, score, total_respondidos

# Função para exibir o ranking dos jogadores, mostrando os 5 melhores.
def mostrar_ranking(ranking):
    print("\n=== Ranking Top 5 Jogadores ===")
    if not ranking:
        print("Nenhum jogo registrado ainda.")
        return
    ranking_ordenado = sorted(ranking, key=lambda x: x[1], reverse=True)
    for i, (nome, pontos) in enumerate(ranking_ordenado[:5], 1):
        print(f"{i}. {nome} - {pontos} pontos")
    print()

# Função principal que controla o menu do jogo.
def main():
    ranking = []

    while True:
        print("\nMenu:")
        print("1 - Jogar")
        print("2 - Ver ranking")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            nome, pontos, total = jogar(estados_capitais)
            if total > 0:
                print(f"Você respondeu {total} estado(s) e fez {pontos} pontos.\n")
                ranking.append((nome, pontos))
            else:
                print("Jogo encerrado sem pontuação.\n")
        elif escolha == "2":
            mostrar_ranking(ranking)
        elif escolha == "3":
            print("Obrigado por jogar. Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()