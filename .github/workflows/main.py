#COIN FLIPPER - PROBABILITY- LAW OF LARGE NUMBERS - STANDART NORMAL
"""
This is a coin flipper program, to calculate probability, mean, median and standart deviance in "x" flips
The texts in the code are in portuguese, because I'm brazilian and that script (and probably every script 
I will write) is only to learn python basics, but if anyone need I can translate it.
"""

import random
import numpy as np

def funcao(flip):
 if flip == 0:
  print("Valor nulo")
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
  if x == 1:
   print("Coroa")
   y = y + 1
   coroas.append(x)
  if x == 0:
   y = y
  if y > flip - 1:
   break
  x = random.randrange(-1, 2)
 if flip != 0:
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
    print("")
    print("A partir do experimento é possivel concluir que quanto mais se aumenta o número de lançamentos, mais nos\naproximamos de uma distribuição normal padrão com média 0 e desvio padrão 1, com probabilidades de cara e\ncoroa se aproximando de 50%")
    print("Para iniciar, insira o número de arremessos. Caso o número seja negativo, o valor absoluto será utilizado")

flip = abs(int(input("Insira o número de arremessos aqui: ")))        
funcao(flip)
def funcao3(flip):
 if flip != 0:
  funcao2(caras, coroas)
funcao3 (flip)
