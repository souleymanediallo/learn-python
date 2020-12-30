def about(name, age, like):
    info = "I am {}. I am {} years old and I like {}.".format(name, age, like)
    return info

dic = {"name": "Souley", "age": 37, "like": "Python"}

print(about(**dic))

print("Hello")

