#Jerdy Bartholomeus 0919350 RAC17-ICTVT1C 03-10-2017
#Opdracht 10

import easygui

easygui.msgbox("U gaat nu een nieuwe helpdesk ticket aanmaken.")
prob = easygui.buttonbox("Kan jij het probleem oplossen?",
                           choices= ["Ja", "Nee"])
if prob == "Ja":
    easygui.msgbox("Los het probleem op.")
    stand_prob = easygui.buttonbox("Is het een standaard probleem?",
                           choices= ["Ja", "Nee"])
    if stand_prob == "Ja":
        easygui.msgbox("Plaats de oplossing in de kennisbank.")
        easygui.msgbox("Sluit de ticket.")
        easygui.msgbox("Verstuur e-mail probleem opgelost.")
    else:
        easygui.msgbox("Sluit de ticket.")
        easygui.msgbox("Verstuur e-mail probleem opgelost.")
else:
    easygui.msgbox("Ticket toekennen aan Software support.")
    easygui.msgbox("Software support werkt eraan.")
    stand_prob2 = easygui.buttonbox("Is het een standaard probleem?",
                           choices= ["Ja", "Nee"])
    if stand_prob2 == "Ja":
        easygui.msgbox("Plaats de oplossing in de kennisbank.")
        easygui.msgbox("Sluit de ticket.")
        easygui.msgbox("Verstuur e-mail probleem opgelost.")
    else:
        easygui.msgbox("Sluit de ticket.")
        easygui.msgbox("Verstuur e-mail probleem opgelost.")