#Advent of Code Day 5 Part 1

input = open(r"2023\Day 6\Day 6 Input.txt", "r")
inputlist = input.readlines()

#These are reference variables. They don't change
cardvalue = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
handname = ["High Card", "One Pair", "Two Pair", "Three of a Kind", "Full House", "Four of a Kind", "Five of a Kind"]
handtype = [11111, 2111, 221, 311, 32, 41, 5]
handsoftype = [[], [], [], [], [], [], []]

#These are adaptable to each input
winningorder = []
# for line in inputlist:
#     winningorder.append(0)

hands = []
handvalues = []
for i in inputlist:
    hands.append(i.strip().split())

#The real start of the script
for i in hands:
    hand = hands.index(i)
    #print("Hand", hand)
    cards = hands[hand][0]
    bet = hands[hand][1]
    jokers = cards.count("J")
    scorecard = []
    handvalue = []
    #print("Hand number", hand, "has cards", cards, "and bet", bet)
    for card in cardvalue:                                                          #Counts the number of each card in the hand
        if cards.count(card) > 0 and card != "J":
            scorecard.append(cards.count(card))
    scorecard = sorted(scorecard, reverse = True)
    #print("Number of jokers found", jokers)
    #print("No jokers", scorecard)
    if jokers == 5:
        scorecard.append(0)
    scorecard[0] += jokers
    #print("With jokers:", scorecard)
    scorecard = int("".join(str(x) for x in (sorted(scorecard, reverse=True))))
    name = handname[handtype.index(scorecard)]
    handsoftype[handtype.index(scorecard)].append(hand)
    for card in cards:
        handvalue.append(cardvalue.index(card))
    handvalues.append(handvalue)
    #print("Hand number", hand, "is a", name, "with value", handvalue)

#print(handsoftype)
for i in handsoftype:
    sortedhands = []
    if len(i) == 1:
        #print(handname[handsoftype.index(i)]+"s", i)
        #print("i is", i)
        winningorder.append(i[0])
    if i and len(i) > 1:
        #print("More than one type of", handname[handsoftype.index(i)], i)
        for hand in i:
            sortedhands.append(handvalues[hand])
        #print(sorted(sortedhands))
        for s in sorted(sortedhands):
            #print("s is:", s)
            winningorder.append(handvalues.index(s))

total = 0
for hand in winningorder:
    rank = winningorder.index(hand) + 1
    bet = int(hands[hand][1])
    score = rank * bet
    #print("Hand", hand, "has rank", rank, "and score", score)
    total += score
print("Total is", total)

        

        
          