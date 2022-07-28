# Find a factorial for any given number

while True:
    number = int(input("Please type in a number: "))
    count = number
    factor = 1
    if number <= 0:
        print("Thanks and bye!")
        break

    while number > 0:
        factor *= number
        number -=1
    
    print(f"The factorial of the number {count} is {factor}")