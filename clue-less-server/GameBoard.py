# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:17:35 2021

@author: M50447
"""

import Token
import Player
import Deck
import Card

class GameBoard:
    def __init__(self):
        self.tokens_lst = []
        self.playerToken_lst = []
        self.weaponToken_lst = []
        self.layoutAdjacencies = {1 : [2,5,11],
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
        self.createTokens()
        self.gameState = 1
        self.playerList = []
        self.playerNames = ["Miss Scarlet", "Colonel Mustard", "Professor Plum", "Mr. Green", "Mrs. White", "Mrs. Peacock"]
        self.roomList = [1,3,5,9,11,13,17,19,21]
        self.roomDict = {1 : "Study",
                         3 : "Library",
                         5 : "Conservatory",
                         9 : "Hall",
                         11 : "Billiard Room",
                         13 : "Ball Room",
                         17 : "Lounge",
                         19 : "Dining Room",
                         21 : "Kitchen"}
        self.suspectNameTokenMapping = {}
        
    # getters
    def getLayoutAdjacencies(self):
        return self.layoutAdjacencies
    
    def getSuspectNameTokenMapping(self):
        return self.suspectNameTokenMapping
    
    def getTokenList(self):
        return self.tokens_lst
    
    def getPlayerList(self):
        return self.playerList
    
    # setters
    def setPlayerList(self, player_lst):
        self.playerList = player_lst
    
    def setGameState(self, num):
        self.gameState = num
    
    # Functions
    def createTokens(self):
        count = 0
        suspectTokens_dict = {"Miss Scarlet" : 14,
                              "Colonel Mustard" : 18,
                              "Professor Plum" : 2,
                              "Mr. Green" : 8,
                              "Mrs. White" : 16,
                              "Mrs. Peacock" : 4}
        weaponTokens = ["Rope","Lead Pipe","Knife","Wrench","Candlestick","Revolver"]
        weapon = 'Weapon'
        suspect = 'Suspect'
        
        for k,v in suspectTokens_dict.items():
            t = Token.Token(k, count, v, suspect)
            self.tokens_lst.append(t)
            self.playerToken_lst.append(t)
            count = count + 1
        for i in weaponTokens:
            t = Token.Token(i, count, 0, weapon)
            self.tokens_lst.append(t)
            count = count + 1
        


    def movePlayer(self, player_token, move_position):
        player_token.setTokenPosition(move_position)
        
    def makeMappings(self):
        suspectNames = ['Miss Scarlet','Colonel Mustard', 'Professor Plum', 'Mr. Green', 'Mrs. White', 'Mrs. Peacock']
        self.suspectNameTokenMapping = dict(zip(suspectNames,self.getTokenList()))
        print(self.suspectNameTokenMapping.items())
        
    def disproveSuggestion(self, p_sug, p_dis, card_lst):
        print(p_dis.name, "It is your turn to disprove the suggestion")
        player_hand = p_dis.hand
        card_names = []
        for i in player_hand:
            card_names.append(i.getCardName())
        card_names = set(card_names)
        suggestion_cards = set(card_lst)
        print(card_names)
        if p_sug is p_dis:
            return print("Skip")
        elif len(card_names.intersection(suggestion_cards)) < 1:
            return print("Skip")
        else:
            common_cards = card_names.intersection(suggestion_cards)
            print("the cards you have in common are: ", common_cards)
            while True:    
                player_input = str(input("which card would you like to show: "))
                if player_input in card_names:
                    return player_input
                else:
                    continue
            
            

        
    
    #
    
    #
    
    #
    