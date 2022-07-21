limit = int(input("Limit: "))
value = 1
sum = 1
word = f"{value}"
while limit > sum:
    value += 1
    sum += value
    word += f" + {value}"
    

print(f"The consecutive sum: {word} = {sum}")