class Personnne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    def sendmail(self, subject, body):
        print(f"To: {self.email}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")

    def __repr__(self):
        return f"{self.nom}, {self.age} ans, {self.email}"


personnes = [
    Personnne('pierre', 25, "pierre@gmail.com"),
    Personnne(nom="paul", age=18, email="app@gmail.com"),
    Personnne("jacques", 52, email="jacque@gmail.com")
]

for personne in personnes:
    print(personne)

index_par_nom = {personne.nom: personne for personne in personnes}

print(index_par_nom)

r = Personnne.sendmail(lambda personnes: personne in p, "hello", "envoie message")
print(r)

# TODO PAGE 8