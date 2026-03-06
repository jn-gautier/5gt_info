mot="anniversaire"
list_lettres_mot=[]
for lettre in mot:
    if lettre not in list_lettres_mot:
        list_lettres_mot.append(lettre)
tentatives_autorisees=len(list_lettres_mot)+3


list_propositions=[]
for i in range(tentatives_autorisees):
    for lettre in mot:
        if lettre in list_propositions :
            print( lettre,end="")
        else:
           print( " _",end="") 
    print("")
    proposition=input("Faites une proposition : ")
    list_propositions.append(proposition)
    if len(proposition)>1:
        if proposition==mot:
            print("Bravo, vous avez gagné WMWMWMW !")
            print(f"Le mot était bien : {mot}")
            break
    
    if set(list_propositions).intersection(set(list_lettres_mot))==set(list_lettres_mot):
        print("Bravo, vous avez gagné WMWMWMW !")
        print(f"Le mot était bien : {mot}")
        break


