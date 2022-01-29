from string import ascii_letters

allowed = set(ascii_letters + ' ')
f = open('file.txt', 'r')
txt = f.read()
#Text must have only letters and spaces
answer = ''.join(l for l in txt if l in allowed)
#Separate the words
x = answer.split()
N = len(x)
sinthiki = x[:]
print("List in the beginning: " + str(sinthiki))
print("Number of words in list in the beginning: " + str(N))
#Initialization for stats
lekseis_tou_1_grammatos = 0
lekseis_twn_2_grammatwn = 0
lekseis_twn_3_grammatwn = 0
lekseis_twn_4_grammatwn = 0
removed_pairs = 0
for i in range(0,N-1,2):
    sum1 = len(sinthiki[i])
    next_word = sinthiki[i+1]
    sum2 = len(next_word)
    #Check if sum of pair = 20
    if (sum1 + sum2) == 20:
        print("Gets removed: " + str(sinthiki[i]))
        x.remove(sinthiki[i])
        print("Gets removed as pair: " + str(next_word))
        x.remove(next_word)
        removed_pairs += 1
        print("----------------")
#Calculating stats
for word in x:
    grammata = len(word)
    if grammata == 1:
        lekseis_tou_1_grammatos += 1
    elif grammata == 2:
        lekseis_twn_2_grammatwn += 1
    elif grammata == 3:
        lekseis_twn_3_grammatwn += 1
    elif grammata == 4:
        lekseis_twn_4_grammatwn += 1
#Output to user
restwords = N - (lekseis_tou_1_grammatos + lekseis_twn_2_grammatwn + lekseis_twn_4_grammatwn + lekseis_twn_3_grammatwn)
print("Edited list: " + str(x))
print("Pairs removed: " + str(removed_pairs))
print("Lista got: " + str(len(x)) + " words!")
print("One letter words: " + str(lekseis_tou_1_grammatos))
print("Two letter words: " + str(lekseis_twn_2_grammatwn))
print("Three letter words: " + str(lekseis_twn_3_grammatwn))
print("Four letter words: " + str(lekseis_twn_4_grammatwn))
print("5 or more letter words:" + str(restwords))
f.close()
