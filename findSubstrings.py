word = input("Please type in a string: ")  #"substringsingsangsung" 
comp = input("Please type in a character: ") #"s" 
rem = word
count = 1
while True:
    result = rem.find(comp)
    extract = rem[result:(result + 3)]
    if len(extract) > 2:
        print(extract)

    if count == 0:
        break
        
    count += result
    rem = rem[(result + 1):]