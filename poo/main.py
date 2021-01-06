sequence = "AlloABk"
for i in range(len(sequence)-1):
    if sequence[i] == "A":
        print(f"C'est {i}")
    elif sequence[i] != "A":
        print(f"Ce n'est pas {i}")


