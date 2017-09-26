#Jerdy Bartholomeus 0919350 RAC17-ICTVT1C 31-08-2017
#Opdracht 3
#Schrijf een programma dat de kosten van de zakelijke directie telefoons berekent met behulp van de volgende gegevens.

Jacob_abo = 45
Jacob_verz = 35
Jacob_bel_sms = 15
kost_Jacob = Jacob_abo + Jacob_verz + Jacob_bel_sms

Fred_abo = 48.50
Fred_verz = 38.75
Fred_bel_sms = 15
kost_Fred = Fred_abo + Fred_verz + Fred_bel_sms

tot_maandkosten = kost_Jacob + kost_Fred
kost_maandcontract = 2 * 12 * tot_maandkosten

print ("De totale kosten van de directie telefoons gedurende het contract bedraagt", int(kost_maandcontract), "euro.")
