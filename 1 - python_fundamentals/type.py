lists = [1,2,4,5, "hello","erhgd", 437,2453]
a = False
b = False
# c = False
j = ""
k = 0
for i in lists:
    if type(i) is str:
        j += i + " "
        a = True
    elif type(i) is int or float:
        k += i
        b = True
if a == True and b == True:
    print "The array you entered is of mixed type"
    print "String: " + j
    print "Sum: " + str(k)
elif b == True and a == False:
    print "The array you entered is of integer type"
    print "Sum: " + str(k)
elif b == False and a == True:
    print "The array you entered is of string type"
    print "String: " + j
