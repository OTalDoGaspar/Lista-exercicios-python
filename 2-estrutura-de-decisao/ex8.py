#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1 <= n2 and n1 <= n3):
    print("recomendo comprar o produto de preço: ", n1)
elif (n2 <= n1 and n2 <= n3):
    print("recomendo comprar o produto de preço: ", n2)
elif (n3 <= n1 and n3 <= n2):
    print("recomendo comprar o produto de preço: ", n3)