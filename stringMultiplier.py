word = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))
result = ""
while amount > 0:
    result += word
    amount -= 1

print(result)