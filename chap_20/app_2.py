def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


num1 = float(input("Num 1 : "))

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

should_continue = True

while should_continue:
    for symbol in operations:
        print(symbol)

    choice_symbol = input("Choose your operation : ")

    num2 = float(input("Num 2 : "))

    func_operations = operations[choice_symbol]
    result = func_operations(num1, num2)

    should_continue = input("Pour continuer taper 'y' ou 'N' pour arrêter : ")

    if should_continue == 'y':
        num1 = result
    else:
        print(result)
        should_continue = False

