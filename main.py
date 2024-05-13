
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



while game_on:

    display()

    user_input = input("Enter the Position to place 'X' : ")
    frst_coord = int(user_input[0])
    scnd_coord = int(user_input[1])

    ttt_list[frst_coord][scnd_coord] = "X"

    display()

    user_input = input("Enter the Position to place 'O' : ")
    frst_coord = int(user_input[0])
    scnd_coord = int(user_input[1])

    ttt_list[frst_coord][scnd_coord] = "O"

    display()





