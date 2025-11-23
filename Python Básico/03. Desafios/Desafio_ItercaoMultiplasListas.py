# Dados duas Listas, printe todos os valores que aparecem
# duplicados nas duas listas.

def valores_duplicados(lista1, lista2):
    """
    Retorna uma lista com os valores que aparecem em ambas as listas, sem repetição.
    Funciona com números, strings ou mistos.
    """
    lista_valores_duplicados = []
    for valor in lista1:
        if valor in lista2 and valor not in lista_valores_duplicados:
            lista_valores_duplicados.append(valor)
    return lista_valores_duplicados

# Dados duas listas, printe uma mensagem dizendo se existe
# algum elemento em comum entre elas ou não.

def existe_valor_comum(lista1, lista2):
    """
    Verifica se existe pelo menos um elemento em comum entre duas listas.
    Imprime mensagem e retorna True/False.
    """
    for valor in lista1:
        if valor in lista2:
            print("Existe pelo menos um elemento em comum.")
            return True
    print("Não existe nenhum elemento em comum.")
    return False

# Adicionado a função abaixo para que valores númericos sejam tratados de forma diferrente de string.
# Se mantiver tudo como string, números "10" e "010" serão considerados diferentes (porque são strings distintas).
# Se precisar comparar valores numéricos com equivalência matemática, é necessário converter para números.

def ler_entrada_mista(mensagem="Digite um valor numérico ou palavra, ou S para sair: "):
    """
    Lê valores do usuário, tentando converter para int; se falhar, mantém string.
    Interrompe se usuário digitar 'S'.
    Retorna lista dos valores lidos (numéricos e/ou strings).
    """
    resultados = []
    while True:
        valor = input(mensagem)
        if valor.upper() == "S":
            break
        try:
            valor_convertido = int(valor)
        except ValueError:
            valor_convertido = valor
        resultados.append(valor_convertido)
        print(f"Você digitou '{valor_convertido}'")
    return resultados

# Código principal

print("Preencha a primeira lista (números, palavras ou mistos).")
lista1 = ler_entrada_mista()

print("\nPreencha a segunda lista (números, palavras ou mistos).")
lista2 = ler_entrada_mista()

duplicados = valores_duplicados(lista1, lista2)
print("\nValores duplicados nas duas listas:", duplicados)

existe_valor_comum(lista1, lista2)