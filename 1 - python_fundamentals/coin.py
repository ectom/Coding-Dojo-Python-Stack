import random
def coin_toss():
    heads = 0
    tails = 0
    print "Starting the program..."
    for i in range(1, 5001):
        a = random.random()
        a = round(a)
        if a == 0:
            tails += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... Got " + str(tails) + " tail(s) so far and " + str(heads) + " head(s) so far"
        if a == 1:
            heads += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... Got " + str(tails) + " tail(s) so far and " + str(heads) + " head(s) so far"
    print "Ending the program, thank you!"
coin_toss()
