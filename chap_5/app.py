class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __repr__(self):
        return f"<< {self.nom}, {self.prenom}, {self.age} >>"

    def sendmail(self, subject, body):
        "Envoie un mail à personne"
        print(f"To : {self.prenom}")
        print(f"Subject : {subject}")
        print(f"Body : {body}")


personnes = [
    Personne('pierre', 'durant', 20),
    Personne(nom="paul", prenom="pierre", age=30),
    Personne("jacques", "lemercier", age=19)
]

for personne in personnes:
    print(personne)

index_par_nom = {personne.nom: personne for personne in personnes}
print(index_par_nom)

pierre = index_par_nom["pierre"]
print(pierre)

