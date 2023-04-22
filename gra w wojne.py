colors = ['Hearts','Diamonds','Clubs','Spades']
# lista + słownik, aby można było działać na listach
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []


for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] =  c
        allCards.append(aCard)
       
import random

random.shuffle(allCards)
print(allCards)

player1 = []

player2 = []


player1 = allCards[:12]
player2 = allCards[12:]

card1 = []
card2 = []

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    
    if card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    elif card1['Power'] < card2['Power']:
        player2.append(card1)
        player2.append(card2)
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
    elif card1["Power"] == card2["Power"]:
        
        player1.append(card1)
        player2.append(card2)
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    ptint('PLAYER 2 WON!!!!')
