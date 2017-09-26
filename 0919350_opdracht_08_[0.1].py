#Jerdy Bartholomeus 0919350 RAC17-ICTVT1C 31-08-2017
#Opdracht 8

import easygui

#1
art_numm = int(easygui.enterbox("Voer hier de artikelnummer in"))
#2
art_naam = easygui.enterbox("Voer hier de naam van de artikel in")
#3
art_prijs = float(easygui.enterbox("Voer hier de prijs van de artikel in"))
#4
korting = float(15/100 *art_prijs)
art_prijs_kort = float(art_prijs - korting)

easygui.msgbox("Uw korting is " + str(korting))
easygui.msgbox("Artikelnummer: " + str(art_numm) + " " + art_naam + " kost normaal " + str(art_prijs) + " euro en nu met 15% korting nog maar " + str(art_prijs_kort) + " euro.")
