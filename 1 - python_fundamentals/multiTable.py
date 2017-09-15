print " x 1 2 3 4 5 6 7 8 9 10 11 12"
for row in range(1, 13):
    string = ''
    for column in range(0, 13):
        if column == 0:
            string += " " + str(row)
        else:
            string += " " + str(column*row)
    print string
