#Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros 
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
# ou em galões de 3,6 litros, que custam R$ 25,00.

#    Informe ao usuário as quantidades de tinta a serem 
#       compradas e os respectivos preços em 3 situações:
#    comprar apenas latas de 18 litros;
#    comprar apenas galões de 3,6 litros;
#    misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#       Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
#       considere latas cheias.
from math import ceil
metros = float(input())

lata1 = 18
lata1Preco = 80
lata2 = 3.6
lata2Preco = 25

litros = metros/6

qntdLatas18 = ceil(litros/lata1)
qntdLatas36 = ceil(litros/lata2)

print(qntdLatas18)
print(qntdLatas36)
print(qntdLatas18 * lata1Preco)
print( qntdLatas36 * lata2Preco)