import pyfiglet
from termcolor import colored
import time
import random


title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

start = time.time()

print("For play with 2 players, please enter 1")
print("For play with computer, please enter 2")

user_choice = int(input("Enter your choice:"))
                  

game_board = [["-", "-", "-"],
              ["-", "-", "-"], 
              ["-", "-", "-"]]

def show_board():
    for row in game_board:
        for col in row:
            if col == "-":
                print("-", end=" ")
            if col == "X":
                print(colored("X", "red"), end=" ")
            if col == "O":
                print(colored("O", "blue"), end=" ")
        print()

def check_game():

    checker_diag= []
    checker_draw= []
    for i in range(3):
        checker_row= []
        checker_col= []

        for j in range(3):
            checker_row.append(game_board[i][j])
            checker_col.append(game_board[j][i])
            checker_draw.append(game_board[i][j])

            if i == j:
                checker_diag.append(game_board[i][j])

            if checker_row == ["X", "X", "X"] or checker_col == ["X", "X", "X"]:
                print("Player 1 Wiiiiiiiiiiiin")
                exit()
            if checker_row == ["O", "O", "O"] or checker_col == ["O", "O", "O"]:
                print("Player 2 Wiiiiiiiiiiiin")
                exit()
    if checker_diag == ["X", "X", "X"]:
        print("Player 1 Wiiiiiiiiiiiin")
        exit()
    if checker_diag == ["O", "O", "O"]:
        print("Player 2 Wiiiiiiiiiiiin")
        exit()

    if "-" not in checker_draw:
        print("Draaaaaaaaaw")
        exit()
            
            
        
if user_choice == 1:

    print(pyfiglet.figlet_format("Player VS Player", font="straight"))
    show_board()

    while True:
        
        
        print("Player 1")
        while True:
            row = int(input("row: "))
            col = int(input("col: "))

            if 0 <= row <= 2  and  0 <= col <= 2:

                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    break

                else:
                    print("jer nazannnnn")
            else:
                print("dorost vared kon dgeeeeee")
        
        show_board()
        check_game()
        
        print("Player 2")
        while True:
            row = int(input("row: "))
            col = int(input("col: "))

            if 0 <= row <= 2  and  0 <= col <= 2:

                if game_board[row][col] == "-":
                    game_board[row][col] = "O"
                    break
                
                else:
                    print("jer nazannnnn")
            else:
                print("dorost vared kon dgeeeeee")

        show_board()
        check_game()




elif user_choice == 2:

    print(pyfiglet.figlet_format("Player VS CPU", font="straight"))
    show_board()


    while True:
        
        
        print("Player 1")
        while True:
            row = int(input("row: "))
            col = int(input("col: "))

            if 0 <= row <= 2  and  0 <= col <= 2:

                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    break

                else:
                    print("jer nazannnnn")
            else:
                print("dorost vared kon dgeeeeee")
        
        show_board()
        check_game()
        
        print("CPU")

        cpu_choice = ["X", "O"]
        row = random.randint(0,2)
        col = random.randint(0,2)

        if game_board[row][col] == "-":
            game_board[row][col] = random.choice(cpu_choice)

        show_board()
        check_game()


else:

    print("Bayad yeli az 2 hlato entekhab mikardi, dobare entekhab kon")


end = time.time()

duration = end - start

print("Runtime is ", duration, " seconds")