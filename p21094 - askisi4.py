import random
from random import randrange

#Nubmer of victories for each player in each sequence
nikes_prwtou = 0
nikes_deuterou = 0
isopalies = 0
nikesprwtou2seq = 0
nikesdeuterou2seq = 0
isopalies2seq = 0
#'21' code from class edited
xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
for periptwsi in range(2):
    #First sequence (Normal share)
    if periptwsi == 0:
        print("Normal share")
        print("-------------")
        #Δημιουργία της τράπουλας
        for l in range(100):
            xartia = []
            figures = ["J", "Q", "K"]
            xarti = [i for i in range(1, 11)] + figures
            color = ["H", "S", "C", "D"]
            for i in xarti:
                for j in color:
                    xartia.append([i, j])
            random.shuffle(xartia)
            player1 = []
            sum1 = 0
            player2 = []
            while sum1<16:
                sum1=0
                player1.append(xartia.pop())
                for card in player1:
                    if card[0] in figures:
                        sum1 = sum1 + 10
                    else:
                        sum1 = sum1 + card[0]
            if sum1>21:
                nikes_deuterou += 1
            else:
                #Second player's turn
                sum2 = 0
                while sum2 < 16:
                    sum2 = 0
                    player2.append(xartia.pop())
                    for card in player2:
                        if card[0] in figures:
                            sum2 = sum2+10
                        else:
                            sum2 = sum2+card[0]
                if sum2 > 21:
                    sum2 = 0
                if sum1 > sum2:
                    nikes_prwtou += 1
                elif sum2>sum1:
                    nikes_deuterou  += 1
                else:
                    isopalies += 1
        print("First Player's wins: " + str(nikes_prwtou))
        print("Second Player's wins: " + str(nikes_deuterou))
        print("Ties: " + str(isopalies))
    #Second sequence, where the players' share is not normal
    else:
        print("+---+---+---+")
        print("Unfair share")
        print("-------------")
        for l in range(100):
            for i in xarti:
                for j in color:
                    xartia.append([i, j])
            random.shuffle(xartia)
            player1 = []
            sum1 = 10 #Player 1 always start with +10
            neodeck = []
            xarti2 = [10] + figures
            for i in xarti2:
                for j in color:
                    neodeck.append([i, j])
            random.shuffle(neodeck)
            flag = True
            while sum1 < 16:
                sum1 = 10
                if flag:
                    pos1 = randrange(len(neodeck))
                    player1.append(neodeck.pop(pos1))
                    for element in player1:
                        if element in xartia:
                            xartia.remove(
                                element)
                    flag = False
                else:
                    player1.append(xartia.pop())
                stop = 0
                for card in player1:
                    if stop == 0:
                        stop += 1
                    else:
                        if card[0] in figures:
                            sum1 = sum1 + 10
                        else:
                            sum1 = sum1 + card[0]
            if sum1 > 21:
                nikesdeuterou2seq += 1
            else:
                player2 = []
                sum2 = 0
                neodeck2 = []
                xarti3 = [i for i in range(1, 10)]
                for i in xarti3:
                    for j in color:
                        neodeck2.append([i, j])
                flag2 = True
                while sum2 < 16:
                    sum2 = 0
                    if flag2:
                        pos2 = randrange(len(neodeck2))
                        player2.append(neodeck2.pop(pos2))
                        for element in player2:
                            if element in xartia:
                                xartia.remove(
                                    element)
                        flag = False
                    else:
                        player2.append(xartia.pop())
                    for card in player2:
                        if card[0] in figures:
                            sum2 = sum2 + 10
                        else:
                            sum2 = sum2 + card[0]
                if sum2 > 21:
                    sum2 = 0
                if sum1 > sum2:
                    nikesprwtou2seq += 1
                elif sum2 > sum1:
                    nikesdeuterou2seq += 1
                else:
                    isopalies2seq += 1
        print("First Player's wins: " + str(nikesprwtou2seq))
        print("Second Player's wins: " + str(nikesdeuterou2seq))
        print("Ties : " + str(isopalies2seq))



