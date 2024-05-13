
ttt_list = [[" ", " ", " " ],
            [" ", " ", " " ],
            [" ", " ", " " ]]

ttt_list[0][2] = "X"

#Display
for row in ttt_list:
    for col in range(len(row)):
        print(f"{row[col]} |")

