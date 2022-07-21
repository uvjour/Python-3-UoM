# Reverse a string
word = input("Please type in a string: ")
count = -1
index = -(len(word))
while count >= index:
    print(word[count])
    count -= 1