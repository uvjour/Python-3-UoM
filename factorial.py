# Find a factorial for any given number

while True:
    number = int(input("Please type in a number: "))
    count = number
    factor = 1
    if number <= 0:
        print("Thanks and bye!")
        break

    while count > 0:
        factor *= count
        count -=1
    
    print(f"The factorial of the number {number} is {factor}")