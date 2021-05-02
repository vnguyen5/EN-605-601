# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:37:18 2021

@author: M50447
"""

import Token
import Card

class Player:
    def __init__(self, name, playerID, token):
        # input we get 
        self.name = name
        self.playerID = playerID
        self.playerState = 0
        self.token = token
        self.movedLastTurn = 0
        self.hand = []
        self.tokenPosition = self.getToken().getTokenPosition()
        
    # getters
    def getName(self):
        return self.name
        
    def getPlayerID(self):
        return self.playerID
    
    def getPlayerState(self):
        return self.playerState
    
    def getPlayerAttrib(self):
        print("Name: ", self.name, " | ","ID: ", self.playerID, " | ","Token Name: ", self.token.getName(), " | ","Token Position: ", self.tokenPosition, " | ")
    
    # you need to specify name or token id when you get the return
    def getTokenID(self):
        return self.token.getTokenID()
    
    def getTokenPosition(self):
        return self.tokenPosition
    
    def getToken(self):
        return self.token
    
    # setters
    def setName(self, name):
        self.name = name
    
    def setPlayerID(self, playerID):
        self.playerID = playerID
        
    def setPlayerState(self, playerState):
        self.playerState = playerState
        
    def setPlayerPosition(self):
        self.tokenPosition = self.getToken().getTokenPosition()
        

    
    
    # player actions
    def makeAccusation(self, card1_name, card2_name, card3_name, CaseFile):
        count = 0
        if self.getPlayerState() != 0:
            return "You cant make an accusation because you are in a losing state!"
        else:
            card_lst = list([card1_name, card2_name, card3_name])
            for i in card_lst:
                if i in CaseFile.caseFileCardList:
                    print("Your card: ", i, " was in the case file")
                    count = count + 1
                else:
                    print("Your card: ", i, "was not in the case file")
            print('Case File Cards:')
            for i in CaseFile.caseFileCardList:
                print(i)
            if count == 3:
                self.setPlayerState(1)
                print(self.name, " you correctly guessed the cards in the case file!")
            else:
                self.setPlayerState = -1
                print(self.name, " you are now in the losing state :(.")
                
        
        
    def movePlayer(self, moveposition, GameBoard):
        if self.getPlayerState() != 0:
            return "You cant move because you are in a losing state!"
        else:
            playerPosition = self.getTokenPosition()
            if moveposition in GameBoard.getLayoutAdjacencies()[playerPosition]:
                self.getToken().setTokenPosition(moveposition)
                self.setPlayerPosition()
                return "Player successfully moved to, ", GameBoard
            else:
                return "You cant move because that is an invalid move position"
            
        
# =============================================================================
#     def makeSuggestion(self, card2_name, card3_name, gameBoard):
#         card1 = self.getRoom()
#         gameBoard.makeSuggestion()
# =============================================================================

        
# =============================================================================
#     def disproveSuggestion(self,)
# =============================================================================

        
                
            
            
        