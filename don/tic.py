import random
from math import inf as infinity

#Stores game markers for X an O's. Default is empty.

markers = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
gameOn = True

#Monitors who won. 

player = "Human"
human_score = 0
ai_score = 0

def print_board():
    print(markers[0], " ¦ ", markers[1], " ¦ ", markers[2])
    print("-------------")
    print(markers[3], " ¦ ", markers[4], " ¦ ", markers[5])
    print("-------------")
    print(markers[6], " ¦ ", markers[7], " ¦ ", markers[8])

#Checks win conditions for game. Needs update scores as global variables and parameters need a different name. 

def game_won(h_score, a_score):
    global human_score, ai_score
    human_score = h_score
    ai_score = a_score

    if markers[0] == markers[1] == markers[2] == "X" or \
       markers[3] == markers[4] == markers[5] == "X" or \
       markers[6] == markers[7] == markers[8] == "X" or \
       markers[0] == markers[3] == markers[6] == "X" or \
       markers[1] == markers[4] == markers[7] == "X" or \
       markers[2] == markers[5] == markers[8] == "X" or \
       markers[0] == markers[4] == markers[8] == "X" or \
       markers[2] == markers[4] == markers[6] == "X" or \
       markers[0] == markers[1] == markers[2] == "O" or \
       markers[3] == markers[4] == markers[5] == "O" or \
       markers[6] == markers[7] == markers[8] == "O" or \
       markers[0] == markers[3] == markers[6] == "O" or \
       markers[1] == markers[4] == markers[7] == "O" or \
       markers[2] == markers[5] == markers[8] == "O" or \
       markers[0] == markers[4] == markers[8] == "O" or \
       markers[2] == markers[4] == markers[6] == "O" :

        if player == "Human":
            human_score += 1
        else:
            ai_score += 1

        print_board()
        print(player, "won!")
        print("Human:", human_score, "AI:", ai_score)
        print("\n")
        reset_game()
    
    if " " not in markers:
        print("Draw! Play again.")
        print("\n")
        reset_game()

    return human_score, ai_score
        
                
def reset_game():
    markers[0] = " " 
    markers[1] = " " 
    markers[2] = " "
    markers[3] = " " 
    markers[4] = " "
    markers[5] = " "
    markers[6] = " "
    markers[7] = " "
    markers[8] = " "


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x in enumerate(state):
        if x != "X" or x != "O":
            cells.append([x])
    
    #for testing
    print(cells)
    return cells
empty_cells(markers)

def minimax(state, depth, player):
    if player == "AI":
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    for cell in empty_cells(markers):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(markers, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == "AI":
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

#AI places marker.
def ai_marker():
    #aiMarker = random.randrange(0,8)
    depth = len(empty_cells(markers))
    aiMarker = minimax(markers, depth, 'AI')
    print(aiMarker)

    while markers[aiMarker] == "X" or markers[aiMarker] == "O":
        aiMarker = random.randrange(0,8)

    markers[aiMarker] = "O"

#Runs game.
while gameOn:
    print_board()
    print("\n")
    newPossition = int(input("Place X marker in possition 1-2-3-4-5-6-7-8-9?" + "\n" + "0 to exit "))
    print("\n")

    #Exits game.
    if newPossition == 0:
        break

    if markers[newPossition-1] == "X" or markers[newPossition-1] == "O":
        print("Try a different possition.")
        print("\n")

    else:
        markers[newPossition-1] = "X"
        print_board()
        player = "Human"
        game_won(human_score, ai_score)
        ai_marker()
        player = "AI"
        game_won(human_score, ai_score)

