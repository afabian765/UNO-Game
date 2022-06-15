import random

def UNOdeck():
    deck = []
    colors = ["Red", "Blue", "Yellow", "Green"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Reverse", "Skip", "Draw Four"]
    wilds = ["Wild", "Wild Draw Four"]
    for color in colors:
        for value in values:
            cardValue = "{} {}".format(color, value)
            deck.append(cardValue)
            if value != 0:
                deck.append(cardValue)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck
    

def shuffleDeck(deck):
    for cardPos in range(len(deck)):
        randPos = random.randint(0, 107)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck

def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn

def showHand(player, playerHand):
    print("Player {} is currently up.".format(player + 1))
    print("Your Hand")
    print("-------")
    y = 1
    for card in playerHand:
        print("{}) {}".format(y, card))
        y += 1
        print(card)
    print("")
        
def Play(color, value, playerHand):
    for card in playerHand:
        if "Wild" in card:
            return True
        elif color in card or value in card:
            return True
    return False

unoDeck = UNOdeck()
unoDeck = shuffleDeck(unoDeck)
discards = []
print(unoDeck)

players = []
colors = ["Blue", "Red", "Yellow", "Green"]
numPlayers = int(input("How many players? "))
while numPlayers < 2 or numPlayers > 4:
    numPlayers = int(input("Not a valid number of players. Please type between 2-4 players."))
for player in range(numPlayers):
    players.append(drawCards(7))

playerTurn = 0
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColor = splitCard[0]
if currentColor != "Wild":
    cardValue = splitCard[1]
else:
    cardValue = "Any"
    
while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card currently on deck: {}".format(discards[-1]))
    if Play(currentColor, cardValue, players[playerTurn]):
        cardChosen = int(input("Which card would you like to put in? "))
    while not Play(currentColor, cardValue, [players[playerTurn][cardChosen-1]]):
        cardChosen = int(input("This card is invalid. Which card do you want to play?"))
    print("You chose {}".format(players[playerTurn][cardChosen-1]))
    discards.append(players[playerTurn].pop(cardChosen-1))
    
    if len(players[playerTurn])==0:
        playing = False
        winner = "Player {}".format(playerTurn+1)
    else:
        splitCard = discards[-1].split(" ", 1)
        currentColor = splitCard[0]
        if len(splitCard) == 1:
            cardValue - "Any"
        else:
            cardValue = splitCard[1]
        if currentColor == "Wild":
            for x in range(len(colors)):
                print("{}) {}".format(x+1, colors[x]))
            newColor = int(input("What color would you like to pick? "))
            while newColor < 1 or newColor > 4:
                newColor = int(input("This option is invalid. Which color would you like to pick? "))
            currentColor = colors[newColor-1]
            if cardValue == "Reverse":
                playDirection = playDirection * -1
            elif cardValue == "Skip":
                playerTurn += playDirection
                if playerTurn >= numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers-1
            elif cardValue == "Draw Two":
                playerDraw = playerTurn + playDirection
                if playerDraw == numPlayers:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = numPlayers-1
                players[playerDraw].extend(drawCards(2))
            elif cardValue == "Draw Four":
                playerDraw = playerTurn + playDirection
                if playerDraw == numPlayers:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = numPlayers-1
                players[playerDraw].extend(drawCards(4))
            print("")
else:
    print("You cant play yet. Your have to draw a card first. ")
    players[playerTurn].extend(drawCards(1))
        

playerTurn += playDirection
if playerTurn == numPlayers:
    playerTurn = 0
elif playerTurn < 0:
    playerTurn = numPlayers-1

print("Game Over")
print("Player {} is the winner!".format(winner))
        


        
    

