# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 20:34:58 2021

@author: M50447
"""
import random
import Card
import CaseFile


class Deck:
    def __init__(self):
        self.cards = []
        self.deckLen = 0
        self.build()
        
    def build(self):
        count = 0
        # make cards for murder weapons
        for i in ["Rope","Lead Pipe","Knife","Wrench","Candlestick","Revolver"]:
            self.cards.append(Card.Card(i,count))
            count = count + 1
        for i in ["Colonel Mustard","Miss Scarlet","Professor Plum","Mr. Green","Mrs. White","Mrs. Peacock"]:
            self.cards.append(Card.Card(i,count))
            count = count + 1
        for i in ["Study","Library","Conservatory","Hall","Billiard Room","Ball Room", "Lounge", "Dining Room", "Kitchen"]:
            self.cards.append(Card.Card(i,count))
            count = count + 1
            
        self.deckLen = len(self.cards)
            
    def show(self):
        for c in self.cards:
            c.show()
    
    
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    
    def buildCaseFile(self):
        murderWeapon = ''
        murderer = ''
        murderRoom = ''
        for i in self.cards:
            if i.getCardID() in [0,1,2,3,4,5]:
                if murderWeapon == '':
                    murderWeapon = i
                    self.cards.remove(i)
                    self.deckLen = self.deckLen - 1
                else:
                    continue
            elif i.getCardID() in [6,7,8,9,10,11]:
                if murderer == '':
                    murderer = i
                    self.cards.remove(i)
                    self.deckLen = self.deckLen - 1
                else:
                    continue
            elif i.getCardID() in [12,13,14,15,16,17,18,19,20]:
                if murderRoom == '':
                    murderRoom = i
                    self.cards.remove(i)
                    self.deckLen = self.deckLen - 1
                else:
                    continue
        casefile = CaseFile.CaseFile(murderWeapon, murderer, murderRoom)
        
        return casefile
    
    def distrubuteCards(self, player_lst):
        count = 0
        print(len(self.cards))
        while self.deckLen > 0:
            c = self.cards.pop(-1)
            print(c.name, count)
            player_lst[count].hand.append(c)
            self.deckLen = self.deckLen - 1
            count = count + 1
            print(self.deckLen)
            if count >= len(player_lst):
                count = 0
                
                
                

            