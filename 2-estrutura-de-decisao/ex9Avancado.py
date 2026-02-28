# Faça um programa que leia três números e mostre-os em ordem decrescente:

nums = [int(input()), int(input()), int(input())]#isso é um array, será explicado na UC de estrutura de dados!

nums.sort(reverse=True)

print(f"{nums[0]} | {nums[1]} | {nums[2]}")