list_one = [1,2,"celery",6,8,4]
list_two = [1,2,"celery",6,8,4]
if len(list_one) != len(list_two):
    print "The lists are not the same"
    exit()
i = 0
while i < len(list_one):
    if list_one[i] != list_two[i]:
        print "The lists are not the same"
        exit()
    i += 1
print "The lists are the same"
