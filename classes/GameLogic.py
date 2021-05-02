# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 19:33:51 2021

@author: M50447
"""

import Deck
import Card
import GameBoard
import Token
import Player
import builtins

#Main function    
if __name__ == '__main__':
    
    print("Welcome to the ClueLess Game!")
    num_of_players = int(input("How many Players are there?"))
    

    layoutAdjacencies_dict = {1 : [2,5,11],
                              2 : [1,3],
                              3 : [2,7,4],
                              4 : [3,5],
                              5 : [11,4,8],
                              6 : [1,9],
                              7 : [3,11],
                              8 : [5,13],
                              9 : [6,10,14],
                              10 : [9,11],
                              11 : [1,5,17,21,7,10,12,15],
                              12 : [11,13],
                              13 : [8,12,16],
                              14 : [9,17],
                              15 : [11,19],
                              16 : [13,21],
                              17 : [14,11,18],
                              18 : [17,19],
                              19 : [18,15,20],
                              20 : [19,21],
                              21 : [11,16,20]}
    
    
    gameBoard = GameBoard.GameBoard(layoutAdjacencies_dict)
    
    player_lst = []
    
    # this will be a list of server inputs
    player_name = ["Shiv", "Edsel", "Thomas", "Nguyen", "Michael", "Megan" ]
    player1, player2, player3, player4, player5, player6 = '','','','','',''
    player_obj_lst = [player1, player2, player3, player4, player5, player6]
    
    for i in range(num_of_players):
        player_obj_lst[i] = Player.Player(player_name[i], i, gameBoard.getTokenList()[i])
        player_lst.append(player_obj_lst[i])
        player_lst[i].getPlayerAttrib()
    
    gameBoard.setPlayerList(player_lst)
    print(gameBoard.getPlayerList())
    
    print()
    Deck = Deck.Deck()
    print("Deck Starting State")
    Deck.show()
    print()
    print("Deck Shuffled")
    Deck.shuffle()
    Deck.show()
    print()
    print("Case File Card IDs")
    CaseFile = Deck.buildCaseFile()
    print()
    print("Case File Card Names")
    for i in CaseFile.caseFileCardList:
        print(i)
    print()
    print("Deck End State: ", Deck.deckLen)
    Deck.show()
    
    cards = Deck.cards
    print(len(player_lst))
    Deck.distrubuteCards(player_lst)
    
    print("Player hands after card distribution")
    for i in player_lst:
        for c in i.hand:
            print(i.name, ": ", c.name)
    
    
    while gameBoard.gameState == 1:
        for p in range(len(player_lst)):
            if gameBoard.gameState == 0:
                break
            print()
            print("It is player: ", player_lst[p].name, "'s turn.")
            while True:
                turnLogic = int(input("Please enter '0' to Move player, '1' to make suggestion, '2' to make accusation, '3' to end your turn: "))
                print()
                if turnLogic < 0:
                    print("The number you enter must be 0 or greater")
                    continue
                elif turnLogic > 3:
                    print("The number you enter must be less than 3")
                    continue
                elif len(str(turnLogic)) > 1:
                    print("The number you enter must be a SINGLE integer between 0 and 3")
                    continue
                else:
                    print()
                    print("User input accepted")
                    break
                    
                    
            if turnLogic == 0:
                while True:
                    currentPosition = player_lst[p].getTokenPosition()
                    print("Your current position is:", currentPosition)
                    print("The possible indexes you can move to are: ", layoutAdjacencies_dict[currentPosition])
                    movePosition = int(input("Please enter a valid move position: "))
                    print()
                    if movePosition not in layoutAdjacencies_dict[currentPosition]:
                        print("You entered: ,", movePosition, ". You must enter one of the following integers: ", layoutAdjacencies_dict[currentPosition])
                        continue
                    usedPositions_lst = []
                    for i in gameBoard.getTokenList():
                        usedPositions_lst.append(i.getTokenPosition())
                    if movePosition in usedPositions_lst:
                        print("There is someone already in location: ", movePosition, " please pick another location.")
                        continue
                    else:
                        break
# =============================================================================
#                 currentPosition = player_lst[i].getTokenPosition()
#                 print("Your current position is:", currentPosition)
#                 print("The possible indexes you can move to are: ", layoutAdjacencies_dict[currentPosition])
#                 movePosition = int(input("Please enter a valid move position: "))
# =============================================================================
                player_lst[p].movePlayer(movePosition, gameBoard)
                print("New Position: ", player_lst[p].getTokenPosition(), " | ", player_lst[p].getName(), " | ", player_lst[p].getToken().getName())
                    
            if turnLogic == 1:
                print("Suggestion Logic is not functional as of now")
                
                
                
                
                
            if turnLogic == 2:
                card1 = input("Please enter the name of the first card you think is in the case file: ")
                card2 = input("Please enter the name of the second card you think is in the case file: ")
                card3 = input("Please enter the name of the thrid card you think is in the case file: ")
                player_lst[p].makeAccusation(card1, card2, card3, CaseFile)
                print(player_lst[p].getPlayerState())
                if player_lst[p].getPlayerState() == 1:
                    print(player_lst[p].name," You are the winner!")
                    print("The game is ending")
                    gameBoard.setGameState(0)
                    print(gameBoard.gameState)
            
            if gameBoard.gameState == 0:
                break
                
            if turnLogic == 3:
                print("Player is passing on turn")
                continue
                
# =============================================================================
#             while True:
#                 try:
#                     turnLogic = int(input("Please enter '0' to Move player, '1' to make suggestion, '2' to make accusation, '3' to end your turn")
#                 except:
#                     print("You must enter a one of the following numbers: Please enter '0' to Move player, '1' to make suggestion, '2' to make accusation, '3' to end your turn")
#                     continue
#                 if turnLogic < 0:
#                     print("The number you enter must be 0 or greater")
#                     continue
#                 elif turnLogic > 3:
#                     print("The number you enter must be less than 3")
#                     continue
#                 elif len(turnLogic) > 1:
#                     print("The number you enter must be an integer between 0 and 3")
#                     continue
#                 else:
#                     print("User input accepted")
#                     break
#                     
# =============================================================================

# =============================================================================
#             if turnLogic == 0:
#                 currentPosition = i.getTokenPosition
#                 print("Your current position is:" currentPosition)
#                 print("The possible indexes you can move to are: ", layoutAdjacencies_dict[currentPosition])
#                 while True:
#                     try:
#                         movePosition = int(input("Please enter the position you want to move: "))
#                     except:
#                         print("You must enter one of the following integers: ", layoutAdjacencies_dict[currentPosition])
#                         continue
#                     if movePosition not in layoutAdjacencies_dict[currentPosition]:
#                         print("You must enter one of the following integers: ", layoutAdjacencies_dict[currentPosition])
#                         continue
#                     usedPositions_lst = []
#                     for i in gameBoard.getTokenList:
#                         usedPositions_lst.append(i.getTokenPosition())
#                     elif movePosition in usedPositions_lst:
#                         print("There is someone already in location: ", movePosition, " please pick another location.")
#                         continue
#                     else:
#                         break
# =============================================================================
                    

            
