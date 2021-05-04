#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets
import Deck
import Card
import GameBoard
import Token
import Player

logging.basicConfig()

STATE = {"value": 0,
         "playerTurn": 0}

USERS = list()
turn_count = 0
player_name = ["Shiv", "Edsel", "Thomas", "Nguyen", "Michael", "Megan" ]

# =============================================================================
# STATE["playerTurn"] = STATE["playerTurn"] % len(USERS)
# =============================================================================

def state_event():
    return json.dumps({"type": "state", **STATE})


def users_event():
    totalUsers = str(len(USERS))
    return json.dumps({"type": "users", "count": len(USERS), "message": "User Added to game. " + totalUsers + " total User(s)"})



async def notify_message(message):
    if USERS:  # asyncio.wait doesn't accept an empty list
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_user(targetUser, message):
    for user in USERS:
        if targetUser == user:
            await user.send(message)


async def register(websocket):
    USERS.append(websocket)
    print(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.pop(websocket)
    await notify_users()


async def messages(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            action = data["action"]
            # Move action for player
            # move action for the gameboard (player to move) during suggestion
            # make suggestion
            # end turn
            # accusation
            if action ==  "start":
                ### go to the message logic and add all the messages you want it to print
                await notify_message(json.dumps({ "message": "Welcome to the Clue-Less Game !!"}))
                num_of_players = len(USERS)
                print(num_of_players)
                    
                # create a gameboard object
                gameBoard = GameBoard.GameBoard()
                gameBoard.makeMappings()
                # this will be replaced with the USERs variable
                player_lst = []
    
                # this will be a list of server inputs
                # Users variable replaces the 
    
                player_name = ["Shiv", "Edsel", "Thomas", "Nguyen", "Michael", "Megan" ]
                player1, player2, player3, player4, player5, player6 = '','','','','',''
                player_obj_lst = [player1, player2, player3, player4, player5, player6]
                
                # creating player object from list, in the api it should be based on users who click start game
                for i in range(len(USERS)):
                    player_obj_lst[i] = Player.Player(player_name[i], i, gameBoard.getTokenList()[i], USERS[i])
                    player_lst.append(player_obj_lst[i])
                    player_lst[i].getPlayerAttrib()
    
                gameBoard.setPlayerList(player_lst)
                print(gameBoard.getPlayerList())
                
                print()
                gameDeck = Deck.Deck()
                print("Deck Starting State")
                gameDeck.show()
                print()
                print("Deck Shuffled")
                gameDeck.shuffle()
                gameDeck.show()
                print()
                print("Case File Card IDs")
                CaseFile = gameDeck.buildCaseFile()
                print()
                print("Case File Card Names")
                for i in CaseFile.caseFileCardList:
                    print(i)
                print()
                print("Deck End State: ", gameDeck.deckLen)
                gameDeck.show()
                attrs = vars(USERS[0])
                await notify_message(json.dumps({ "message": "It is, {}. turn.".format(player_name[turn_count])}))
                await notify_message(json.dumps(STATE))
                print(STATE)
                STATE["playerTurn"] = STATE["playerTurn"] + 1 % len(USERS)
                await notify_message(json.dumps(STATE))
                print(STATE)
                

            
            
            if action == "minus":
                STATE["value"] -= 1
                await notify_state()
            elif action == "plus":
                STATE["value"] += 1
                await notify_state()
            else:
                print("unsupported event: ", data)
                await notify_message(message)
    finally:
        # print(error)
        await unregister(websocket)







start_server = websockets.serve(messages, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
