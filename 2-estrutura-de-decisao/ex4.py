# Faça um programa que verifique se uma letra digitada é vogal ou consoante.

import string

vogais = "aeiou"
print(string.ascii_lowercase)
l = input()

if (l in vogais):
    print("Vogal")
elif (l in string.ascii_lowercase): #string.ascii_lowercase == "abcdefghijklmnopqrstuvwxyz"
    print("Consoante")
else:
    print("Caractére inválido")