
ttt_list = [["0", "0", "0" ],
            ["0", "0", "0" ],
            ["0", "0", "0" ]]

ttt_list[0][2] = "X"
ttt_list[1][1] = "X"
ttt_list[2][0] = "X"

#Display
for i, row in enumerate(ttt_list):
    for j, item in enumerate(row):
        if j == 2:
            print(item, end=" ")
        else:
            print(item, end=" | ")
    print()
    if i == 2:
        print()
    else:
        print("----------")




