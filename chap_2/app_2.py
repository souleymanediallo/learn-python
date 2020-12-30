import tkinter as tk

racine = tk.Tk()

print(dir(racine))

label = tk.Label(racine, text="J'adore Python")
bouton = tk.Button(racine, text="Quitter", fg="red", commad=racine.destroy)






