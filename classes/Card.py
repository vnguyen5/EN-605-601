# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 19:44:20 2021

@author: M50447
"""

class Card:
    def __init__(self, name, cardID):
        self.name = name
        self.cardID = cardID
        
    def show(self):
        print("Card Name: ", self.name, "| Card ID: ", self.cardID)
        
    def getCardName(self):
        return self.name
    
    def getCardID(self):
        return self.cardID
    