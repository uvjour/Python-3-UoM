
number = int(input("Please type in a number: "))
count = 1
while count <= number:
    if number <= 0:
        break

    if count == number:
        print(number)
        break
    else:
        print(count+1)
        print(count)
        count += 2