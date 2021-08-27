import re

# write your code here
some_text_in_table = [[" "] * 3, [" "] * 3, [" "] * 3]
print(some_text_in_table)
print(some_text_in_table[0][1])


def printing_grid(table):
    print("---------")
    for i in range(0, 3):
        print("| ", end="")
        for j in range(0, 3):
            print(table[i][j], "", end="")
        print("|", end="\n")
    print("---------")


def move(table):
    game = True
    three_in_a_row = ["XXX", "OOO"]
    circle_or_cross = ["X"]
    counter = 0
    while game:
        if counter > 8:
            print("Draw")
            break
        coordinates = input("Enter the coordinates: ")
        while not re.match(r"\d\s\d", coordinates):
            print("You should enter numbers!")
            coordinates = input("Enter the coordinates: ")
        else:
            while not re.match(r"[1-3]\s[1-3]", coordinates):
                print("Coordinates should be from 1 to 3!")
                coordinates = input("Enter the coordinates: ")
            else:
                while not table[int(coordinates[0]) - 1][int(coordinates[2]) - 1] == " ":
                    print("This cell is occupied! Choose another one!")
                    coordinates = input("Enter the coordinates: ")
                else:
                    table[int(coordinates[0]) - 1][int(coordinates[2]) - 1] = circle_or_cross[0]
                    printing_grid(some_text_in_table)
                    if (some_text_in_table[0][0] + some_text_in_table[1][0] + some_text_in_table[2][0] in three_in_a_row or
                            some_text_in_table[0][1] + some_text_in_table[1][1] + some_text_in_table[2][1] in three_in_a_row or
                            some_text_in_table[0][2] + some_text_in_table[1][2] + some_text_in_table[2][2] in three_in_a_row or
                            some_text_in_table[0][0] + some_text_in_table[0][1] + some_text_in_table[0][2] in three_in_a_row or
                            some_text_in_table[1][0] + some_text_in_table[1][1] + some_text_in_table[1][2] in three_in_a_row or
                            some_text_in_table[2][0] + some_text_in_table[2][1] + some_text_in_table[2][2] in three_in_a_row or
                            some_text_in_table[0][0] + some_text_in_table[1][1] + some_text_in_table[2][2] in three_in_a_row or
                            some_text_in_table[2][0] + some_text_in_table[1][1] + some_text_in_table[0][2] in three_in_a_row):
                            print(circle_or_cross[0], "wins")
                            game = False
                    if circle_or_cross[0] == "X":
                        circle_or_cross[0] = "O"
                    else:
                        circle_or_cross[0] = "X"
                    counter += 1

printing_grid(some_text_in_table)
move(some_text_in_table)
