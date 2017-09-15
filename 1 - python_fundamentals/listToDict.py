name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    if len(arr1) >= len(arr2):
        for i in arr1:
            for k in arr2:
                new_dict[i] = k
        print new_dict
    elif:
        for i in arr2:
            for k in arr1:
                new_dict[i] = k
        print new_dict
print make_dict(name, favorite_animal)
