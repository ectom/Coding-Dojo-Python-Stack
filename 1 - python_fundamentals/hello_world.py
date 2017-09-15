words = "It's thanksgiving day. It's my birthday,too!"
x = [2,54,-2,7,12,98]
y = ["hello",2,54,-2,7,12,98,"world"]
z = [19,2,54,-2,7,12,98,32,10,-3,6]

print words.find('day')
print words.replace('day','month')
print min(x)
print max(x)
print y[0]
print y[len(y)-1]
a = [y[0], y[len(y)-1]]
print a
z.sort()
b = len(z)/2
c = z[:b]
d = z[b:]
d.insert(0, c)
print d
