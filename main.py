
ttt_list = [[" ", " ", " " ],
            [" ", " ", " " ],
            [" ", " ", " " ]]

game_on = True


def display():
    count = 0
    print("    (0) (1) (2)")
    print()
    for i, row in enumerate(ttt_list):
        for j, item in enumerate(row):
            if j == 0:
                print(f"({count}) ", end=" ")
                count += 1

            if j == 2:
                print(item, end=" ")
            else:
                print(item, end=" | ")
        print()
        if i == 2:
            print()
        else:
            print("     ---------")
    return ttt_list


def check():
    for i in range(0,3):
        if ttt_list[i][0] == ttt_list[i][1] == ttt_list[i][2] != " ":
            print(f"{ttt_list[i][0]} wins bro")
            return False
        elif ttt_list[0][i] == ttt_list[1][i] == ttt_list[2][i] != " ":
            print(f"{ttt_list[0][i]} wins bro")
            return False
    if ttt_list[0][0] == ttt_list[1][1] ==  ttt_list[2][2] != " ":
        print(f"{ttt_list[0][0]} wins bro")
        return False
    if ttt_list[0][2] == ttt_list[1][1] ==  ttt_list[2][0] != " ":
        print(f"{ttt_list[0][2]} wins bro")
        return False
    else:
        return True



def first_coord():
    return int(user_input[0])


def second_coord():
    return int(user_input[1])


while game_on:
    display()
    game_on = check()

    if not game_on:
        break

    user_input = input("Enter the Position to place 'X' : ")
    frst_coord = first_coord()
    scnd_coord = second_coord()

    ttt_list[frst_coord][scnd_coord] = "X"

    display()
    game_on = check()

    if not game_on:
        break

    user_input = input("Enter the Position to place 'O' : ")
    frst_coord = first_coord()
    scnd_coord = second_coord()

    ttt_list[frst_coord][scnd_coord] = "O"





