# Dado uma sequência de números, calcule a soma e a média dos números.
# ATENÇÃO: Não value usar a função sum()

def soma_media(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista) if len(lista) > 0 else 0
    return soma, media

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: Não value usar a função max()

def maior_numero(lista):
    if len(lista) == 0:
        return None  # lista vazia
    num_max = lista[0]
    for num in lista[1:]:
        if num > num_max:
            num_max = num
    return num_max

# Dado uma lista de palavras, printe todas palavras com pelo menos 5 caracteres.

def maior5_letras(lista):
    if len(lista) == 0:
        print("A lista está vazia.")
        return
    print("Palavras com 5 ou mais letras:")
    encontrou = False
    for palavra in lista:
        if len(palavra) >= 5:
            print(palavra)
            encontrou = True
    if not encontrou:
        print("Nenhuma palavra com 5 ou mais letras foi digitada.")

# Função para leitura dos números da lista de Soma e média, bem como para identificar o maior número.

def ler_numeros():
    lista = []
    while True:
        valor = input("Digite um valor numérico ou S para sair: ")
        if valor.upper() == "S":
            break
        try:
            numero = int(valor)
            lista.append(numero)
            print(f"Você digitou o número {numero}")
        except ValueError:
            print("Entrada inválida, por favor digite um número ou S para sair.")
    return lista

# Função para leitura das palavras.

def ler_palavras():
    lista = []
    while True:
        valor = input("Digite uma palavra ou S para sair: ")
        if valor.upper() == "S":
            break
        lista.append(valor)
        print(f"Você digitou a palavra '{valor}'")
    return lista

# Funções que irão chamar as outras funções do código dependendo da escolha do usuário.

def opcao_soma_media():
    lista = ler_numeros()
    if not lista:
        print("Lista vazia, não é possível calcular soma e média.")
        return
    soma, media = soma_media(lista)
    print("A soma da lista é:", soma)
    print("A média da lista é:", media)

def opcao_maior_numero():
    lista = ler_numeros()
    if not lista:
        print("Lista vazia, não é possível encontrar o maior número.")
        return
    num_max = maior_numero(lista)
    print("O maior número da lista é:", num_max)

def opcao_palavras_com_5():
    lista = ler_palavras()
    if not lista:
        print("Lista vazia, não há palavras para mostrar.")
        return
    maior5_letras(lista)

#Código principal

def main():
    while True:
        escolha = input("Escolha uma opção:\n" \
                        "1 - Soma e Média\n" \
                        "2 - Maior número\n" \
                        "3 - Palavras com 5 ou mais letras\n" \
                        "Outro - Sair\n")
        if escolha == "1":
            opcao_soma_media()
        elif escolha == "2":
            opcao_maior_numero()
        elif escolha == "3":
            opcao_palavras_com_5()
        else:
            print("Saindo do programa. Até mais!")
            break

if __name__ == "__main__":
    main()