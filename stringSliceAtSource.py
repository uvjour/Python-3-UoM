word = input("Please type in a string: ")
comp = input("Please type in a character: ")
result = word.find(comp)
extract = word[result:(result + 3)]
if len(extract) > 2:
    print(extract)