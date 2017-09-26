#Jerdy Bartholomeus 0919350 RAC17-ICTVT1C 31-08-2017
#Opdracht 7

import easygui

printer = easygui.buttonbox("Welke merk printer heeft u?",
                            choices = ['Canon', 'HP', 'Siemens'])
easygui.msgbox ("U heeft " + printer + " gekozen")
ip_adres = easygui.buttonbox("Welke ip adres heeft uw printer?",
                            choices = ['1.1.1.1', '2.2.2.2', '3.3.3.3'])
easygui.msgbox ("U heeft de " + printer + " gekozen met de ip adres " + ip_adres + ".")
