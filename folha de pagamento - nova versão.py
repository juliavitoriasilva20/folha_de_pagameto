import math

salarioB = float(input("Digite o salário: "))
vale = input("Descontar o vale transporte:")




if salarioB <1302.00:
    inss = salarioB*0.075
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído sem INSS é de: R$", (salarioB-inss))
elif salarioB <2571.29:
    inss = salarioB*0.09
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído é de: R$", (salarioB-inss))
elif salarioB <3856.94:
    inss = salarioB*0.12
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído é de: R$", (salarioB-inss))
elif salarioB <7507.50:
    inss = salarioB*0.14
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído é de: R$", (salarioB-inss))
elif salarioB >3856.95:
    inss = salarioB-876.95
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído é de: R$", (salarioB-inss))

if  vale == "s" or vale == "s":
  valVale = salarioL * 0.06
  salarioL = salarioL - valVale
  print ("seu salário líquido é de: R$",(salarioB-inss-valVale))
  salarioL = salarioL - valVale
  print ("Seu salário é de: R$", salarioL)
  
  
  
