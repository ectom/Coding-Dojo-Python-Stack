import random
def grades():
    for i in range(11):
        a = random.random()*(100-60)+60
        if a >= 90:
            print "Score: " + str(int(a)) + "; Your grade is A"
        if a >= 80 and a <= 89:
            print "Score: " + str(int(a)) + "; Your grade is B"
        if a >= 70 and a <= 79:
            print "Score: " + str(int(a)) + "; Your grade is C"
        if a >= 60 and a <= 69:
            print "Score: " + str(int(a)) + "; Your grade is D"
grades()
