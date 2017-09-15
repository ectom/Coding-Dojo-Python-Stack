my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
def dictToTuple(dict):
    newList = []
    for i in dict:
        newList.append((i, dict[i]))
    return newList

print dictToTuple(my_dict)
