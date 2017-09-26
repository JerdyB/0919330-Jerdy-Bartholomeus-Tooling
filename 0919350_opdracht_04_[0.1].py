#Jerdy Bartholomeus 0919350 RAC17-ICTVT1C 31-08-2017
#Opdracht 4

import math

jaarrente = 11.2
maandrente = round (1 +11.2 /100/12-1*100, 2)

uitkomst = math.pow(jaarrente,maandrente)

print ("De maandrente bedraagt", uitkomst, "bij een jaarrente van", jaarrente, ".")
