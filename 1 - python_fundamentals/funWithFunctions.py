def odd_even():
    for i in range (0,2001):
        if i % 2 == 0:
            print "Number is " + str(i) + " this is an even number"
        else:
            print "Number is " + str(i) + " this is an odd number"

def multiply(arr, num):
    for i in range (len(arr)):
        arr[i] *= num
    return arr


def layered_multiples(a):
    new_list = []
    for idx in range (len(a)):
        temp_list = []
        for i in range (a[idx]):
            temp_list.append(1)
        new_list.append(temp_list)
    return new_list
