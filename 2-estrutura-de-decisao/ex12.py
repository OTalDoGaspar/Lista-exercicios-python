# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR: - Salário Bruto até 900 (inclusive) - isento - Salário Bruto até 1500 (inclusive) - desconto de 5% - Salário Bruto até 2500 (inclusive)
# desconto de 10% - Salário Bruto acima de 2500 - desconto de 20%

# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Salário Bruto: (5 * 220)        : R$ 1100,00
# (-) IR (5%)                     : R$   55,00
# (-) INSS ( 10%)                 : R$  110,00
# FGTS (11%)                      : R$  121,00
# Total de descontos              : R$  165,00
# Salário Liquido                 : R$  935,00

gh = float(input())
qh = float(input())

salarioBruto = gh * qh

inss = salarioBruto* 0.1

if (salarioBruto < 900):
    ir = 0
elif (salarioBruto < 1500):
    ir = 0.05
elif (salarioBruto < 2500):
    ir = 0.1
else:
    ir = 0.2

desconto = (salarioBruto*ir) + inss
print(f"salarioBruto: ({gh} * {qh}) :R${round(salarioBruto, 2)}")
print(f"(-) IR: ({ir*100}%) :R${round(salarioBruto * ir, 2)}")
print(f"(-) INSS: (10%) :R${round(inss, 2)}")
print(f"FGTS: (11%) :R${round(salarioBruto * 0.11)}")
print(f"Total de descontos: :R${round(desconto, 2)}")
print(f"Salário Líquido: :R${round(salarioBruto - desconto, 2)}")

