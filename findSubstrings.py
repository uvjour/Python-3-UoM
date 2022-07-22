word = "incomprehensibilities" #input("Please type in a string: ")
comp = "i" #input("Please type in a character: ")
rem = word
count = 1
while True:
    result = rem.find(comp)
    extract = rem[result:(result + 3)]
    if len(extract) > 2:
        print(extract)

    if len(rem) == 2:
        break
        
    count += result
    rem = rem[(result + 1):]