# The program prints out a list of multiplication operations until both operands reach the number given by the user.

number = int(input("Please type in a number: "))
j = 1
while j <= number:
    i = 1
    while i <= number:
        print(f"{j} x {i} = {i * j}")
        i += 1
    if i == number and j == number:
            break
    j += 1