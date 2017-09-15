#Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for i in range (1,1000):
    if i % 2 == 0:
        continue
    print i
#Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000
for i in range (5, 1000000):
    if i % 5 == 0:
        print i
#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
k = 0
for i in a:
    k = k + i
print k

#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

print k/len(a)
