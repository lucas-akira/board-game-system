from menu import *
from BoardGame import *
from piece import *
from player import *
from action import *
from procedures import *
from turn import *
from victory import *
from grid import *

def game():
    board,actions=start_menu()
    players=[]
    for k in range(board.number_players):
        nomjoueur=input("Nom du joueur {}".format(k))
        players.append(player(nomjoueur))
        k=0
    if board.verify_go_each_turn==y:
        while not victory(board.grid, board.length_to_win)[0]:
            turn = turn()
            turn.player = players[k]
            k = (k+1)%board.number_players
            turn.actions = actions
            turn.ask_action()
            turn.execute_action()
            print(grid_to_string_with_size(board.grid, board.height))
        print("Victoire de {}".format(victory(board.grid, board.length_to_win)[1]))
    else:
        while not is_grid_full(board.grid):
            turn = turn()
            turn.player = players[k]
            k = (k+1)%board.number_players
            turn.actions = actions
            turn.ask_action()
            turn.execute_action()
            print(grid_to_string_with_size(board.grid, board.height))
        if victory(board.grid,board.length_to_win)[0]:
            print("Victoire de {}".format(victory(board.grid, board.length_to_win)[1]))


