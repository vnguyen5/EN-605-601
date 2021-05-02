# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:21:43 2021

@author: M50447
"""

class Token:
    def __init__(self, name, tokenID, tokenPosition, tokenType):
        self.name = name
        self.tokenID = tokenID
        self.tokenPosition = tokenPosition
        self.tokenType = tokenType
# =============================================================================
#         self.room = room
# =============================================================================
        
    # Getters
    def getName(self):
        return self.name
    
    def getTokenID(self):
        return self.tokenID
    
    def getTokenPosition(self):
        return self.tokenPosition
    
    def getTokenType(self):
        return self.tokenType
    
    # Setters
    def setName(self, name):
        self.name = name
    
    def setTokenID(self, tokenID):
        self.tokenID = tokenID
    
    def setTokenPosition(self, tokenPosition):
        self.tokenPosition = tokenPosition
    
    def setTokenType(self, tokenType):
        self.tokenType = tokenType
        
        
    # Functions
    def show(self):
        print("Name: ", self.getName(), " | Token ID: ", self.getTokenID(), " | Token Position: ", self.getTokenPosition(), " | Token Type: ", self.getTokenType())
    