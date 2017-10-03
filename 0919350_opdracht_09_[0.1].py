#Jerdy Bartholomeus 0919350 RAC17-ICTVT1C 03-10-2017
#Opdracht 9

import easygui

enq_vraag = easygui.buttonbox("Uw bestelling is afgerond. Heeft u tijd voor een korte enquete?",
                  choices = ["Ja", "Nee"])
if enq_vraag == "Nee":
    easygui.msgbox("Dankuwel voor uw bestelling.")
    print("Uw bestelling is afgerond. Heeft u tijd voor een korte enquete?: " + enq_vraag)
else:
    enq_bereid = easygui.buttonbox("Bent u bereidt 3 vragen te beantwoorden?",
                      choices = ["Ja", "Nee"])
    print("Uw bestelling is afgerond. Heeft u tijd voor een korte enquete?: " + enq_vraag)
    print("Bent u bereidt 3 vragen te beantwoorden?: " + enq_bereid)
    if enq_bereid == "Nee":
        easygui.msgbox("Bedankt voor uw tijd.")
    else:
        easygui.msgbox("Alvast bedankt voor uw medewerking.")
        enq_mv = easygui.buttonbox("Bent u een man of een vrouw?",
                          choices= ["Man", "Vrouw"])
        print("Bent u een man of een vrouw?: " + enq_mv)
        enq_lc = easygui.buttonbox("In welke leeftijdscategorie zit u?",
                          choices= ["18-30", "31-60", "61+"])
        print("In welke leeftijdscategorie zit u?: " + enq_lc)
        enq_Ned = easygui.buttonbox("Woont u in Nederland?",
                          choices= ["Ja", "Nee"])
        print("Woont u in Nederland?: " + enq_Ned)