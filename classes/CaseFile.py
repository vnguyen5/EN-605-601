# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 19:57:26 2021

@author: M50447
"""

class CaseFile:
    # murder weapon, murderer, and murder room are all going to be of type card
    def __init__(self, murderWeapon, murderer, murderRoom):
        self.murderWeapon= murderWeapon
        self.murderer = murderer
        self.murderRoom = murderRoom
        self.caseFileCardList = list([self.murderWeapon.name, self.murderer.name, self.murderRoom.name])
        
        
    # getters        
    def getMurderWeaponName(self):
        return self.murderWeapon.show()
        
# =============================================================================
#     def getMurderWeaponCardID(self):
#         
#         
#     # Setters
#     def setMurderWeapon(self, weapon_card):
#         
#     def setMurderRoom(self, room_card):
#         
#     def setMurderer(self, murderer_card):
#         
#     def compareTo(self, Player)
# =============================================================================
        
