#Faça um programa que peça o raio de um círculo, calcule e mostre sua área:

import math

r = float(input())

area = round(math.pi, 2) * (r**2)

print(area)