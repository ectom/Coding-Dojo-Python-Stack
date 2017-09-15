users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
     ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}
print "Students"
count1 = 0
count2 = 0
for k in users["Students"]:
    print count1 + 1, " - " , users["Students"][count1]['first_name'], " " ,users["Students"][count1]['last_name'], " - " , len(users["Students"][count1]['first_name']) + len(users["Students"][count1]['last_name'])
    count1 += 1
print "Instructors"
for k in users["Instructors"]:
    print count2 + 1 , " - " , users["Instructors"][count2]['first_name'], " " , users["Instructors"][count2]['last_name'] , " - " , len(users["Instructors"][count2]['first_name']) + len(users["Instructors"][count2]['last_name'])
    count2 += 1
