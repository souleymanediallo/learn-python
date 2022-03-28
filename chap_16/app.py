print("""
Choisissez un nombre de 1 à 3 (ou 0 pour terminer)
""")
ch = input()
a = int(ch)
while a:
    if a == 1:
        print("Vous avez choisi un : ")
    elif a == 2:
        print("Vous preférez le deux : ")
    elif a == 3:
        print("Vous avez choisi le plus grand des 3")
    else:
        print("Choisissez un nombre entre un et trois, s.v.p")
    a = int(input())
print("Vous avez entre zéro !")
print("L'exercice est donc termniné !")