word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

i = 0
while i < len(word_list):
    for k in word_list[i]:
        if k == char:
            new_list.append(word_list[i])
    i += 1
print new_list
