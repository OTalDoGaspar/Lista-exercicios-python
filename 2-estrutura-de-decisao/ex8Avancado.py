#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

nums = [float(input()), float(input()), float(input())]#isso é um array, será explicado na UC de estrutura de dados!

nums.sort()

print(f"recomendo comprar o produto de preço: {nums[0]}")