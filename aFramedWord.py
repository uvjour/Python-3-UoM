# This program outputs any word you provide to it framed with asterisks

word = input("Word: ")
count = 30
print("*" * 30)
rem = count - len(word)
left = int((rem / 2) - 1)
if ((rem - (left*2)) == 2):
    print("*"+ (" " * left) + word + (" " * left) + "*")
else:
    print("*"+ (" " * left)+ word + (" " * left)+ " *")
print("*" * 30)