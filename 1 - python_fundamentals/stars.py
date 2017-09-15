def stars(arr):
    for i in range(len(arr)):
        star = ""
        for k in range(arr[i]):
            star += "*"
        print star
stars([1,5,8,2])

def stars2(arr):
    for i in range(len(arr)):
        star = ""
        if type(arr[i]) == int:
            for k in range(arr[i]):
                star += "*"
        elif type(arr[i]) == str:
            for k in range(len(arr[i])):
                star += arr[i][:1].lower()
        print star
stars2([1,"Tom",5,8,"hfe8wso",2])
