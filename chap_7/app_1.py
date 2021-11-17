class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    def __repr__(self):
        return f"Nom : {self.nom}, Age : {self.age}, Email : {self.email}"


personnes = [
    Personne('Pierre', 25, 'pierre@foo.com'),
    Personne('Ousmane', 35, 'ousmane@foo.com'),
    Personne('Malick', 20, 'malick@foo.com'),
]

index_par_nom = {personne.nom: personne for personne in personnes}
print(index_par_nom)
print("=============================")
p = index_par_nom["Pierre"]
print(p)
