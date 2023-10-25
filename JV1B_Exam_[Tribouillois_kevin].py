
#exercice 1

tailletableau=int(input("veuillez saisir la taille du tableau.\n"))
case="_|"
casedubas=" |"
multiplicateur=tailletableau-1

for n in range(tailletableau-1):
    print(case*multiplicateur,"_")
    
for n in range(tailletableau-1):
    print(casedubas, end="")


