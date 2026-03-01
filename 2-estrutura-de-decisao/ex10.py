# Faça um programa que pergunte em que turno você estuda. Peça para digitar:
#     M - Matutino
#     V - Vespertino
#     N - Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

l = input().lower()

if (l ==  "M"):
    print("Bom Dia!")
elif (l == "V"):
    print("Boa Tarde!")
elif (l == "N"):
    print("Boa Noite!")
else:
    print("Valor Inválido!")