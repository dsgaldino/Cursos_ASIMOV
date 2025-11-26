# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.

def cifra_de_cesar(texto, chave):
    alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultado = ''
    
    for chacaracter in texto:
        if chacaracter in alfabeto_minusculo:
            indice = alfabeto_minusculo.index(chacaracter)
            novo_indice = (indice + chave) % 26
            resultado += alfabeto_minusculo[novo_indice]
        elif chacaracter in alfabeto_maiusculo:
            indice = alfabeto_maiusculo.index(chacaracter)
            novo_indice = (indice + chave) % 26
            resultado += alfabeto_maiusculo[novo_indice]
        else:
            # Mantém acentos, espaços e pontuação inalterados
            resultado += chacaracter
    return resultado

while True:
    print("\nEscolha a opção:")
    print("1 - Cifrar texto")
    print("2 - Decifrar texto")
    print("3 - Sair")
    escolha = input("Digite o número da opção: ")
    
    if escolha == '1':
        texto = input("Digite o texto para cifrar: ")
        chave = int(input("Digite a chave (número inteiro): "))
        print("Texto cifrado:", cifra_de_cesar(texto, chave))
    elif escolha == '2':
        texto = input("Digite o texto para decifrar: ")
        chave = int(input("Digite a chave usada para cifrar: "))
        print("Texto decifrado:", cifra_de_cesar(texto, -chave))
    elif escolha == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")