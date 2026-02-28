#Faça um programa que leia três números e mostre o maior deles:

#Solução mais otimizada com conceitos mais avançados...

nums = [int(input()), int(input()), int(input())]#isso é um array, será explicado na UC de estrutura de dados!

nums.sort()

print(nums[2])