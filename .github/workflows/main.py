#COIN FLIPPER - PROBABILITY- LAW OF LARGE NUMBERS - STANDART NORMAL
"""
This is a coin flipper program, to calculate probability, mean, median and standart deviance in "x" flips
Also, I shoul say it isn't complete. I don't know why, but sometimes it flips the coin 1 time more than I 
wanted. If anyone know how to fix it, feel free to contact me. But I don't want to import any other package
or use other command but "randrange" from random, because the idea is learn how to use this command.
The texts in the code are in portuguese, because I'm brazilian and that script (and probably every script 
I will write) is only to learn python basics, but if anyone need I can translate it.
"""

import random
import numpy as np

def funcao(flip):
 y = 0
 global caras
 caras = []
 global coroas
 coroas = []
 x = random.randrange(-1, 2)
 while y != flip:
  if x == -1:
   print("Cara")
   y = y + 1
   caras.append(x)
   x = random.randrange(-1, 2)
  if x == 1:
   print("Coroa")
   y = y + 1
   coroas.append(x)
   x = random.randrange(-1, 2)
  if x == 0:
   y = y
   x = random.randrange(-1, 2) 
  if y > flip - 1:
   break
 z = caras + coroas
 z_array = np.array(z)
 print("")
 print("O número de caras obtido nos " + str(flip) + " lançamentos foi " + str(len(caras)) + ".")
 print("")
 print("O número de coroas obtido nos " + str(flip) + " lançamentos foi " + str(len(coroas)) + ".")
 print("")
 print("A mediana dos lançamentos é " + str(np.median(z_array)))
 print("")
 print("A média dos lançamentos é " + str(np.mean(z_array)))
 print("")
 print("O desvio padrão dos lançamentos é " + str(np.std(z_array)))
 print("")

def funcao2(caras, coroas):
    cap = caras + coroas
    porcentagem_caras = (len(caras) / len(cap)) * 100
    porcentagem_coroas = (len(coroas) / len(cap)) * 100
    print("O percentual de caras apresentado é " + str(porcentagem_caras) + "%")
    print("")
    print("O percentual de coroas apresentado é " + str(porcentagem_coroas) + "%")

flip = int(input("Insira o número de arremessos aqui: "))        
funcao(flip)
funcao2(caras, coroas)
print("")
print("A partir do experimento é possivel concluir que quanto mais se aumenta o número de lançamentos, mais nos\naproximamos de uma distribuição normal padrão com média 0 e desvio padrão 1, com probabilidades de cara e\ncoroa se aproximando de 50%")
