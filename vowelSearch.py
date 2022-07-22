# This program searches the vowels a, e and o in a string provided to it. Can be amended to create a dynamic search function

word = input("Please type in a string: ")
comp = ["a", "e", "o"]
count = 0
while count <= (len(comp)-1):
    if comp[count] in word:
        print(f"{comp[count]} found")
    else:
        print(f"{comp[count]} not found")
    count +=1