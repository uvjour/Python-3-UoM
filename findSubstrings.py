word = "stringsingsang" #input("Please type in a string: ")
comp = "s" #input("Please type in a character: ")
rem = word
count = 1
while count < len(word):
    result = rem.find(comp)
    extract = rem[result:(result + 3)]
    if len(extract) > 2:
        print(extract)

    if len(rem) < 2:
        break
        
    rem = rem[(count):]
    count += result