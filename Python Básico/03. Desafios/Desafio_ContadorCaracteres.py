# Crie um codigo que conta números de vogais de um bloco de texto qualquer.
# O código deve considerar letras maiúscula/minúsculas, isto é, "a" e "A" 
# da mesma forma
# O texto pode sr colado diretamente como um string no código


texto = """

O texto possui 6 vogais A
O texto possui 6 vogais E
O texto possui 11 vogais I
O texto possui 21 vogais O
O texto possui 6 vogais U

"""

texto_formatado = texto.lower()
vogais = "aeiou"

contador_vogais = {v: 0 for v in vogais}

for letra in texto_formatado:
    if letra in contador_vogais:
        contador_vogais[letra] += 1
        
for v in vogais:
    print(f"O texto possui {contador_vogais[v]} vogais {v.upper()}")