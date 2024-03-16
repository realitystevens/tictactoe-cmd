import time


gameBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'bottom-L': ' ', 'bottom-M': ' ', 'bottom-R': ' '}


def print_gameBoard(gameBoard):
    print(f"{gameBoard['top-L']} | {gameBoard['top-M']} | {gameBoard['top-R']}")
    print('- + - + -')
    print(f"{gameBoard['mid-L']} | {gameBoard['mid-M']} | {gameBoard['mid-R']}")
    print('- + - + -')
    print(f"{gameBoard['bottom-L']} | {gameBoard['bottom-M']} | {gameBoard['bottom-R']}")


while True:
    print("\nGuidelines to play the game. \nType in the position you want to play as the input \n\n- Use the table illustration below to get the positioning for the game play. \n[top-L, top-M, top-R] \n[mid-L, mid-M, mid-R] \n[bottom-L, bottom-M, bottom-R] \n\nEnsure you read through \n\nReady to play? (YES/NO)")
    play = input()

    if play == 'YES':
        break
    elif play == 'NO':
        print("Alright, go through the instructions again.")
        time.sleep(1)
        continue
    else:
        continue

turn = "X"

for i in range(9):
    print(f"Turn for {turn} to make a play. \nType in the position you want to play.")
    print_gameBoard(gameBoard)
    
    move = input()

    while True:
        if move == "":
            print('Ensure you enter an input')
            move = input()
            time.sleep(1)
            continue
        elif move == " ":
            print('Ensure you enter an input')
            move = input()
            time.sleep(1)
            continue
        else:
            break

    gameBoard[move] = turn

    if turn == "X":
        turn = "O"
    else:
        turn = "X"


print_gameBoard(gameBoard)
