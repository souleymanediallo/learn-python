choices = []
for pos in range(0, 9):
    choices.append(str(pos + 1))

Is_current_One = True

while True:
    print(choices[0] + '|' + choices[1] + '|' + choices[2])
    print("-----")
    print(choices[3] + '|' + choices[4] + '|' + choices[5])
    print("-----")
    print(choices[6] + '|' + choices[7] + '|' + choices[8])

    try:
        choice = int(input("> ").strip())
    except ValueError:
        print("Please enter valid field")
        continue

    if Is_current_One:
        choices[choice - 1] = 'X'
    else:
        choices[choice - 1] = 'O'

    Is_current_One = not Is_current_One

    for pos_x in range(0, 3):
        pos_y = pos_x * 3

    if (choices[pos_y] == choices[(pos_y + 1)]) and (choices[pos_y] == choices[(pos_y + 2)]):
        print("Your are winner")
        break

    if (choices[pos_x] == choices[(pos_x + 3)]) and (choices[pos_x] == choices[(pos_x + 6)]):
        print("Your are winner")
        break







