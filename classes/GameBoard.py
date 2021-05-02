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
    def __init__(self,  layoutAdjacencies_dict):
        self.tokens_lst = []
        self.playerToken_lst = []
        self.weaponToken_lst = []
        self.layoutAdjacencies = layoutAdjacencies_dict
        self.createTokens()
        self.gameState = 1
        self.playerList = []

        
    # getters
    def getLayoutAdjacencies(self):
        return self.layoutAdjacencies
    
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
        
        


        
        
        
    
    #
    
    #
    
    #
    