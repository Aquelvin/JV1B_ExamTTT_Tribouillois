listeA=[0,0,0]
listeB=[0,0,0]
listeC=[0,0,0]


for n in range(9):
    print("   1  2  3")
    print("A",listeA)
    print("B",listeB)
    print("C",listeC)
    choix=input("Où voulez vous placer une croix? (veillez répondre par la lettre de la rangée en MAJUSCULE suivit du nombre de la colonne.)\n")
    if (choix=="A1"or choix=="A2"or choix=="A3"):
        if (choix=="A1"):
            listeA[0]="X"
        if (choix=="A2"):
            listeA[1]="X"
        if (choix=="A3"):
            listeA[2]="X"
    
    if (choix=="B1"or choix=="B2"or choix=="B3"):
        if (choix=="B1"):
            listeB[0]="X"
        if (choix=="B2"):
            listeB[1]="X"
        if (choix=="B3"):
            listeB[2]="X"

    if (choix=="C1"or choix=="C2"or choix=="C3"):
        if (choix=="C1"):
            listeC[0]="X"
        if (choix=="C2"):
            listeC[1]="X"
        if (choix=="C3"):
            listeC[2]="X"

print("   1  2  3")
print("A",listeA)
print("B",listeB)
print("C",listeC)
'''
    choix=input("Où voulez vous placer une rond? (veillez répondre par la lettre de la rangée en MAJUSCULE suivit du nombre de la colonne.)\n")
    if (choix=="A1"or choix=="A2"or choix=="A3"):
        if (choix=="A1"):
            listeA[0]="O"
        if (choix=="A2"):
            listeA[1]="O"
        if (choix=="A3"):
            listeA[2]="O"

    if (choix=="B1"or choix=="B2"or choix=="B3"):
        if (choix=="B1"):
            listeB[0]="O"
        if (choix=="B2"):
            listeB[1]="O"
        if (choix=="B3"):
            listeB[2]="0"

    if (choix=="C1"or choix=="C2"or choix=="C3"):
        if (choix=="C1"):
            listeC[0]="O"
        if (choix=="C2"):
            listeC[1]="O"
        if (choix=="C3"):
            listeC[2]="O"
'''

