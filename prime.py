number = int(input("Enter Number: "))

if_prime = True

for divisor in range(2, number):
    if (number % divisor) == 0:
        is_prime = False
        break

    if is_prime:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")
