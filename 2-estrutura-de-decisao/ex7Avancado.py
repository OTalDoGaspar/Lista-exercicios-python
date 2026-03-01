# Faça um programa que leia três números e mostre o maior e o menor deles:

#Solução mais otimizada com conceitos mais avançados...

nums = [int(input()), int(input()), int(input())]#isso é um array, será explicado na UC de estrutura de dados!

nums.sort()

print(nums[0])
print(nums[2])