#Faça um programa que leia três números e mostre o maior deles:

n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1 >= n2 and n1 >= n3):
    print(n1)
    if(n2 <= n3):
        print(n2)
    else:
        print(n3)
elif (n2 >= n1 and n2 >= n3):
    print(n2)
    if(n1 <= n3):
        print(n1)
    else:
        print(n3)
elif (n3 >= n1 and n3 >= n2):
    print(n3)
    if(n1 <= n2):
        print(n1)
    else:
        print(n2)