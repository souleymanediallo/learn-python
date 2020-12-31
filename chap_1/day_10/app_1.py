def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Vous n'avez pas completer tous les elements"

    format_f_name = f_name.capitalize()
    format_l_name = l_name.capitalize()
    return f"{format_f_name} {format_l_name}"


print(format_name(input("What's your first_name : "), input("What's your last_name : ")))
